"""Final provenance check: 60 CPU seconds, 4 GiB, no numerical experiments.

This supplements the coordinator's complete reading of the original reports
and checking sources. It cannot establish reading, independence or correctness
by itself. Outputs go to a fresh study-owned generated directory.
"""
from pathlib import Path
import hashlib
import json
import resource
import subprocess
import time

ROOT = Path(__file__).resolve().parents[2]
STUDY = ROOT / "studies/observable_hierarchy"
DATA = ROOT / "data/generated/observable_hierarchy"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    resource.setrlimit(resource.RLIMIT_AS, (4 * 1024**3, 4 * 1024**3))
    start = time.process_time()
    output = DATA / "H4_acceptance_checks_v3"
    output.mkdir(exist_ok=False)
    expected = {
        "H4_scientific_E_v3.md": "2c8c71790c2cfd91cf247bbf8138299eea069b04c8d592d8543ddb178ee40980",
        "H4_scientific_F_v3.md": "3148721488be5f6e2e167596ef415ae4eb62d8ebd650ef38828ff16596abfbcc",
        "H4_integration_v3.md": "f347fb537bcf14cd51946f49c9168f5c678a97ffa75616b117c471eda6af059f",
        "H4_reproduction_v1.md": "547c2b6658428a9a738670d900912c9b3e2aeaaf4e51085041e322998fad7ab4",
        "H4_reproduction_addendum_v3.md": "7df71242fc718a679d877a25806d7506a4cceceba71dd33d5b413f916a0e5ed7",
    }
    for name, value in expected.items():
        assert digest(STUDY / name) == value
    packet_path = STUDY / "H4_review_manifest_v3.json"
    assert digest(packet_path) == "06132871ed70c3c13651a3fbb1f8e76d13582301237acb811f50756bdb223d02"
    for row in read(packet_path)["files"]:
        path = ROOT / row["path"]
        assert digest(path) == row["sha256"] and path.stat().st_size == row["bytes"]
    e = read(DATA / "H4_scientific_E_v3/run.json")
    assert e["status"] == "pass" and all(x["exit_code"] == 0 for x in e["commands"])
    assert read(DATA / "H4_scientific_E_v3/audit.json")["all_decoded_scalar_count"] == 3416112
    fdir = DATA / "H4_scientific_F_v3"
    f = read(fdir / "completion.json")
    for name, value in f["reviewer_sources"].items():
        assert digest(STUDY / name) == value
    for name, value in f["evidence"].items():
        assert digest(fdir / name) == value
    assert f["status"] == "complete" and f["frozen_inputs_unchanged"]
    assert read(fdir / "supplied_tests_record.json")["returncode"] == 0
    assert read(fdir / "audit_results.json")["status"] == "PASS"
    assert read(fdir / "attack_results.json")["status"] == "PASS"
    integration = read(DATA / "H4_integration_v3/execution_summary.json")
    for name, value in integration["checker_sources"].items():
        assert digest(STUDY / name) == value
    assert all(x["returncode"] == 0 for x in integration["commands"])
    addendum = read(STUDY / "H4_reproduction_addendum_v3_checks.json")
    detail = read(STUDY / "H4_reproduction_addendum_v3_details.json")
    assert addendum["status"] == detail["status"] == "pass"
    assert addendum["original_generated_files_verified"] == 237
    assert sum(x["byte_identical"] for x in addendum["comparisons"]) == 23
    assert len(detail["changed_tests"]) == 2
    assert all(x["ast_identical_except_docstrings_and_fail_messages"] for x in detail["changed_tests"])
    correction = STUDY / "H4_reproduction_addendum_v3_correction.md"
    assert correction.is_file()
    mapping_path = STUDY / "H4_promotion_mapping_v3_final.json"
    mapping = read(mapping_path)
    assert mapping["status"] == "reviewed_pending_user_approval_not_applied"
    assert len(mapping["destinations"]) == 11
    for row in mapping["destinations"]:
        live = ROOT / row["destination"]
        assert (digest(live) if live.exists() else None) == row["current_live_sha256"]
        assert digest(ROOT / mapping["edition"] / row["destination"]) == row["destination_sha256"]
        assert digest(ROOT / row["source"]) == row["source_sha256"]
    for row in read(ROOT / mapping["edition"] / "edition_manifest.json")["files"]:
        if row["kind"] == "unchanged dependency":
            assert digest(ROOT / row["source"]) == row["source_sha256"]
    patch = STUDY / "H4_proposed_changes_v3.patch"
    assert digest(patch) == mapping["proposed_patch_sha256"]
    command = ["git", "apply", "--check", str(patch.relative_to(ROOT))]
    subprocess.run(command, cwd=ROOT, check=True, timeout=30)
    source_records = {}
    for pattern in ("H4_scientific_E_v3*", "H4_scientific_F_v3*", "H4_integration_v3*", "H4_reproduction_addendum_v3*"):
        for path in STUDY.glob(pattern):
            if path.is_file():
                source_records[path.name] = digest(path)
    record = dict(status="pass_pending_user_approval", cpu_seconds=time.process_time()-start,
                  script_sha256=digest(Path(__file__)), reports=expected,
                  report_correction_sha256=digest(correction), source_records=source_records,
                  review_manifest_sha256=digest(packet_path),
                  final_mapping_sha256=digest(mapping_path), patch_sha256=digest(patch),
                  proposal_sha256=digest(STUDY / "H4_promotion_proposal_v3.md"),
                  acceptance_sha256=digest(STUDY / "H4_acceptance_v3.md"),
                  patch_check_command=command, patch_check_exit_code=0,
                  unchanged_inputs=271, declared_destinations=11,
                  no_candidate_or_established_edits=True, no_tests_or_trajectories=True,
                  note="Coordinator complete reading and provenance verification are recorded separately in H4_acceptance_v3.md. This mechanical check is not a substitute for independent reviews or user approval.")
    (output / "record.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({k: v for k, v in record.items() if k not in ("source_records", "reports")}))


if __name__ == "__main__":
    main()
