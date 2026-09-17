"""Synthetic retention-guard checks. No checkpoint is actually deleted."""
import json
from pathlib import Path
import sys
from unittest.mock import patch

import numpy as np

import RETIRE as helper


def main():
    output = helper.path_in_campaign(sys.argv[1]) if len(sys.argv) > 1 else helper.CAMPAIGN / "retention_fixture_001"
    output.mkdir(exist_ok=False)
    helper.CAMPAIGN = output
    (output / "manifest.json").write_text(json.dumps({"sources_sha256": {
        str(helper.HERE.relative_to(helper.ROOT) / "NETWORK.py"): helper.sha256(helper.HERE / "NETWORK.py")}}))
    inputs = output / "inputs.npz"
    np.savez(inputs, synthetic=np.array([0.0]))
    reports, directories = {}, {}
    for name, count in (("old", 2), ("new", 3)):
        directory = output / name
        directory.mkdir()
        directories[name] = directory
        (directory / "state.pt").write_bytes(("fabricated guard-test bytes " + name).encode())
        values = dict(times=5*np.arange(count), predictions=np.zeros((count, 3)), loss=np.zeros(count),
                      grams=np.zeros((count, 2, 1, 1)), rms=np.zeros((count, 2)), movement=np.zeros((count, 2)),
                      dense_predictions=np.zeros(4))
        np.savez(directory / "trajectories.npz", **values)
        config = dict(kind="network", stage="synthetic_guard_check", width=9, seed=11, dtype="float64", h=.02,
                      obs_dt=5, inputs_path=str(inputs), id=name, t_min=0, t_max=values["times"][-1].item())
        hashes = {key: helper.sha256(directory / key) for key in ("state.pt", "trajectories.npz")}
        record = dict(status="complete", config=config, config_hash=helper.config_hash(config),
                      last_time=values["times"][-1].item(), source_hash=helper.sha256(helper.HERE / "NETWORK.py"),
                      inputs_hash=helper.sha256(inputs), output_hashes=hashes,
                      initialization_hashes={key: "a"*64 for key in ("a", "b", "c")},
                      checks=dict(all_finite=True, checkpoint_state_exact=True, checkpoint_prediction_replay_error=0),
                      scope="Fabricated metadata guard test; this is not a model run or numerical verification.")
        if name == "new":
            record["resume_from"] = str(directories["old"] / "state.pt")
        record_path = directory / "record.json"
        record_path.write_text(json.dumps(record))
        job = dict(passed=True, kind="network", directory=str(directory), config=config,
                   last_time=record["last_time"], record_sha256=helper.sha256(record_path),
                   initialization_hashes=record["initialization_hashes"],
                   hashes={key: dict(path=str(directory / key), passed=True, actual=value, expected=value)
                           for key, value in hashes.items()},
                   replay=dict(performed=True, passed=True, checkpoint_metadata_exact=True, max_error=0))
        if name == "new":
            old_hash = helper.sha256(directories["old"] / "state.pt")
            job["hashes"]["resume_state"] = dict(path=record["resume_from"], passed=True, actual=old_hash, expected=old_hash)
        report = dict(passed=True, verifier_source_sha256=next(iter(helper.APPROVED_VERIFIERS)), jobs={name: job},
                      scope="Fabricated metadata guard test; no independent model replay is claimed.")
        reports[name] = output / (name + "_verification.json")
        reports[name].write_text(json.dumps(report))
    old, new = directories["old"] / "state.pt", directories["new"] / "state.pt"
    original_files = {str(path): helper.sha256(path) for path in output.rglob("*") if path.is_file()}
    prepared = helper.prepare(old, new, reports["old"], reports["new"])
    descriptor = Path(prepared["descriptor"])
    outcomes = {"prepare_preserves_every_existing_file": all(helper.sha256(path) == expected for path, expected in original_files.items()),
                "prepare_does_not_delete": old.exists() and new.exists(),
                "descriptor_is_read_only": descriptor.stat().st_mode & 0o222 == 0}

    def refused_after_mutation(label, path, value):
        original = path.read_bytes()
        old_stat = path.stat()
        try:
            path.write_bytes(value)
            with patch.object(helper.os, "unlink", side_effect=AssertionError("unexpected deletion attempt")) as unlink:
                try:
                    helper.execute(descriptor)
                    outcomes[label] = False
                except ValueError:
                    outcomes[label] = unlink.call_count == 0
        finally:
            path.write_bytes(original)
            helper.os.utime(path, ns=(old_stat.st_atime_ns, old_stat.st_mtime_ns))

    refused_after_mutation("changed_old_state_refused_before_unlink", old, b"changed")
    refused_after_mutation("changed_successor_refused_before_unlink", new, b"changed")
    refused_after_mutation("changed_report_refused_before_unlink", reports["new"], b"{}")
    unapproved = json.loads(reports["new"].read_text())
    unapproved["verifier_source_sha256"] = "b"*64
    refused_after_mutation("unapproved_verifier_version_refused", reports["new"], json.dumps(unapproved).encode())
    record_path = directories["new"] / "record.json"
    original_record = json.loads(record_path.read_text())
    for label, change in (("failed_child_refused", dict(status="failed")),
                           ("wrong_parent_refused", dict(resume_from=str(new))),
                           ("nonincreasing_time_refused", dict(last_time=5))):
        changed = dict(original_record, **change)
        refused_after_mutation(label, record_path, json.dumps(changed).encode())
    changed = dict(original_record)
    changed["config"] = dict(changed["config"], h=.01)
    changed["config_hash"] = helper.config_hash(changed["config"])
    refused_after_mutation("changed_step_refused", record_path, json.dumps(changed).encode())
    for label, value in (("traversal_refused", output / "old/../new/state.pt"),
                         ("outside_campaign_refused", helper.ROOT / "state.pt")):
        try:
            helper.path_in_campaign(value)
            outcomes[label] = False
        except ValueError:
            outcomes[label] = True
    symlink = output / "symlink_state.pt"
    symlink.symlink_to(old)
    try:
        helper.path_in_campaign(symlink)
        outcomes["symlink_refused"] = False
    except ValueError:
        outcomes["symlink_refused"] = True
    # Reach the sole unlink call only through a mock that raises before touching
    # the filesystem. This exercises the valid execution guard without deletion.
    class DeletionDisabled(RuntimeError):
        pass
    captured = {}
    def deletion_disabled(target, *, dir_fd):
        captured.update(target=target, directory_inode=helper.os.fstat(dir_fd).st_ino)
        raise DeletionDisabled()
    with patch.object(helper.os, "unlink", side_effect=deletion_disabled) as unlink:
        try:
            helper.execute(descriptor)
            outcomes["valid_execution_targets_only_old_file"] = False
        except DeletionDisabled:
            outcomes["valid_execution_targets_only_old_file"] = (unlink.call_count == 1 and captured["target"] == old.name
                and captured["directory_inode"] == old.parent.stat().st_ino)
    outcomes["no_checkpoint_actually_deleted"] = old.exists() and new.exists()
    outcomes["no_completion_receipt_without_deletion"] = not helper.receipt_path(old).exists()
    original_exists, original_regular, original_read_json = Path.exists, helper.regular_file, helper.read_json
    def hide_old(path):
        return False if path == old else original_exists(path)
    with patch.object(Path, "exists", hide_old):
        try:
            helper.historical_evidence(old, helper.sha256(old))
            outcomes["missing_state_without_receipt_refused"] = False
        except (ValueError, FileNotFoundError):
            outcomes["missing_state_without_receipt_refused"] = True
    fake_receipt = dict(schema=helper.SCHEMA, status="retired", descriptor_sha256=helper.sha256(descriptor),
                        old_checkpoint=str(old), old_sha256=helper.sha256(old), old_checkpoint_present=False,
                        successor_checkpoint=str(new), successor_sha256=helper.sha256(new))
    receipt = helper.receipt_path(old)
    def simulated_regular(path):
        return old.stat() if path == receipt else original_regular(path)
    def simulated_json(path):
        return fake_receipt if Path(path) == receipt else original_read_json(path)
    with patch.object(Path, "exists", hide_old), patch.object(helper, "regular_file", simulated_regular), patch.object(helper, "read_json", simulated_json):
        historical = helper.historical_evidence(old, helper.sha256(old))
        outcomes["historical_attestation_never_claims_live_hash_or_replay"] = (
            historical["passed"] is True and historical["checkpoint_replayable"] is False
            and historical["observed_live_state_hash"] is False and "actual" not in historical
            and historical["live_terminal_checkpoint"] == str(new))
        try:
            helper.historical_evidence(old, helper.sha256(old), visited={old})
            outcomes["retirement_cycle_refused"] = False
        except ValueError:
            outcomes["retirement_cycle_refused"] = True
    def hide_both(path):
        return False if path in (old, new) else original_exists(path)
    with patch.object(Path, "exists", hide_both), patch.object(helper, "regular_file", simulated_regular), patch.object(helper, "read_json", simulated_json):
        try:
            helper.historical_evidence(old, helper.sha256(old))
            outcomes["missing_terminal_successor_refused"] = False
        except (ValueError, FileNotFoundError):
            outcomes["missing_terminal_successor_refused"] = True
    result = dict(passed=all(outcomes.values()), checks=outcomes, actual_deletions=0,
                  helper_source_sha256=helper.sha256(helper.__file__),
                  check_source_sha256=helper.sha256(__file__),
                  scope="Fabricated guard fixtures; no training, model validation, or checkpoint deletion.")
    (output / "check_result.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    return 0 if result["passed"] else 2


if __name__ == "__main__":
    sys.exit(main())
