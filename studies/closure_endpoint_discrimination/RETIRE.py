"""Prepare or execute retirement of one verified superseded NETWORK checkpoint.

Preparation is the default and never deletes. Execution is a separate explicit
invocation. Only campaign_001/.../state.pt may be removed; all supporting files
are retained. Historical attestations never assert a deleted file is replayable.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import math
import os
from pathlib import Path
import stat

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CAMPAIGN = ROOT / "data/generated/closure_endpoint_discrimination/campaign_001"
INVARIANTS = ("kind", "stage", "width", "seed", "dtype", "h", "obs_dt")
HISTORY = ("times", "predictions", "loss", "grams", "rms", "movement")
SCHEMA = "network-checkpoint-retirement-v1"
APPROVED_VERIFIERS = {"d10347192c17c135494d7d18b3d06d070bb79ee895bb507154b76a1043d63a90"}


def fail(condition, message):
    if not condition:
        raise ValueError(message)


def path_in_campaign(value):
    raw = Path(value)
    fail(".." not in raw.parts, "parent traversal is forbidden")
    if not raw.is_absolute():
        raw = ROOT / raw
    path = Path(os.path.abspath(raw))
    fail(path == path.resolve(), f"symlink components are forbidden: {path}")
    fail(path.is_relative_to(CAMPAIGN), f"path is outside the current campaign: {path}")
    return path


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text())


def config_hash(config):
    return hashlib.sha256(json.dumps(config, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def regular_file(path):
    path = path_in_campaign(path)
    info = path.lstat()
    fail(stat.S_ISREG(info.st_mode) and info.st_nlink == 1, f"requires a regular file with one link: {path}")
    return info


def identity(path):
    info = regular_file(path)
    return dict(device=info.st_dev, inode=info.st_ino, size=info.st_size, mtime_ns=info.st_mtime_ns)


def report_job(report_path, directory, record, expected_hashes, require_parent_hash=None):
    report_path = path_in_campaign(report_path)
    regular_file(report_path)
    report = read_json(report_path)
    fail(report.get("passed") is True, "verification report did not pass")
    fail(report.get("verifier_source_sha256") in APPROVED_VERIFIERS,
         "verification report is not from an approved verifier version")
    matches = [(name, job) for name, job in report.get("jobs", {}).items()
               if path_in_campaign(job.get("directory", "")) == directory]
    fail(len(matches) == 1, "verification report must contain exactly one matching job")
    name, job = matches[0]
    fail(job.get("passed") is True and job.get("kind") == "network", "matching verification job did not pass as a network")
    fail(job.get("config") == record["config"] and job.get("last_time") == record["last_time"],
         "verification job does not bind the checkpoint configuration/time")
    fail(job.get("record_sha256") == sha256(directory / "record.json"), "verification report record hash differs")
    fail(job.get("initialization_hashes") == record["initialization_hashes"], "verification initialization evidence differs")
    for key, expected in expected_hashes.items():
        evidence = job.get("hashes", {}).get(key, {})
        fail(evidence.get("passed") is True and evidence.get("actual") == expected and evidence.get("expected") == expected
             and path_in_campaign(evidence.get("path", "")) == directory / key,
             f"verification report lacks a fresh bound hash for {key}")
    replay = job.get("replay", {})
    fail(replay.get("performed") is True and replay.get("passed") is True
         and replay.get("checkpoint_metadata_exact") is True and replay.get("max_error") == 0,
         "retirement requires independent exact dense checkpoint replay")
    if require_parent_hash is not None:
        evidence = job.get("hashes", {}).get("resume_state", {})
        fail(evidence.get("passed") is True and evidence.get("actual") == require_parent_hash
             and evidence.get("expected") == require_parent_hash
             and path_in_campaign(evidence.get("path", "")) == path_in_campaign(record["resume_from"]),
             "child verification does not bind the parent hash observed during verification")
    return dict(path=str(report_path), sha256=sha256(report_path), job=name,
                verifier_source_sha256=report["verifier_source_sha256"])


def checkpoint_record(checkpoint, require_live):
    checkpoint = path_in_campaign(checkpoint)
    fail(checkpoint.name == "state.pt", "only a file named state.pt is eligible")
    directory = checkpoint.parent
    record_path, trajectories = directory / "record.json", directory / "trajectories.npz"
    regular_file(record_path)
    regular_file(trajectories)
    record = read_json(record_path)
    config = record.get("config", {})
    fail(record.get("status") == "complete" and config.get("kind") == "network", "only a complete successful network is eligible")
    fail(not (directory / "failure.json").exists(), "failure evidence makes checkpoint retirement ineligible")
    fail(all(key in config for key in INVARIANTS), "checkpoint configuration lacks required invariants")
    fail(record.get("config_hash") == config_hash(config), "checkpoint configuration hash differs")
    fail(isinstance(record.get("last_time"), (int, float)) and math.isfinite(record["last_time"]) and record["last_time"] >= 0,
         "invalid checkpoint time")
    frozen = read_json(CAMPAIGN / "manifest.json")
    expected_source = frozen["sources_sha256"][str(HERE.relative_to(ROOT) / "NETWORK.py")]
    fail(record.get("source_hash") == expected_source and sha256(HERE / "NETWORK.py") == expected_source,
         "checkpoint is not from the frozen network producer")
    inputs = path_in_campaign(config["inputs_path"])
    fail(record.get("inputs_hash") == sha256(inputs), "checkpoint input hash differs")
    checks = record.get("checks", {})
    fail(checks.get("all_finite") is True and checks.get("checkpoint_state_exact") is True
         and checks.get("checkpoint_prediction_replay_error") == 0, "producer checkpoint correctness checks failed")
    outputs = record.get("output_hashes", {})
    fail(set(outputs) >= {"state.pt", "trajectories.npz"}, "checkpoint output hashes are missing")
    fail(all(isinstance(outputs[key], str) and len(outputs[key]) == 64 for key in ("state.pt", "trajectories.npz")),
         "malformed checkpoint hashes")
    fail(sha256(trajectories) == outputs["trajectories.npz"], "trajectory bytes differ from the successful record")
    if require_live:
        regular_file(checkpoint)
        fail(sha256(checkpoint) == outputs["state.pt"], "checkpoint bytes differ from the successful record")
    init_hashes = record.get("initialization_hashes", {})
    fail(set(init_hashes) == {"a", "b", "c"} and all(isinstance(value, str) and len(value) == 64 for value in init_hashes.values()),
         "initial PCG64 hashes are incomplete")
    binding = dict(checkpoint=str(checkpoint), sha256=outputs["state.pt"], time=record["last_time"],
                   record_path=str(record_path), record_sha256=sha256(record_path),
                   trajectories_path=str(trajectories), trajectories_sha256=outputs["trajectories.npz"],
                   config_hash=record["config_hash"], source_hash=record["source_hash"],
                   inputs_hash=record["inputs_hash"], initialization_hashes=init_hashes)
    return record, binding


def evidence(old, new, old_report, new_report, require_old=True, require_new=True):
    old, new = path_in_campaign(old), path_in_campaign(new)
    fail(old != new, "old and new checkpoint are identical")
    old_record, old_binding = checkpoint_record(old, require_old)
    new_record, new_binding = checkpoint_record(new, require_new)
    fail(path_in_campaign(new_record.get("resume_from", "")) == old, "successor is not a direct continuation of this checkpoint")
    fail(new_record["last_time"] > old_record["last_time"], "successor must be strictly later")
    for key in INVARIANTS:
        fail(old_record["config"][key] == new_record["config"][key], f"trajectory invariant differs: {key}")
    for key in ("source_hash", "inputs_hash", "initialization_hashes"):
        fail(old_record[key] == new_record[key], f"trajectory invariant differs: {key}")
    with np.load(old.parent / "trajectories.npz", allow_pickle=False) as left, np.load(new.parent / "trajectories.npz", allow_pickle=False) as right:
        count = len(left["times"])
        fail(len(right["times"]) > count and float(left["times"][-1]) == old_record["last_time"]
             and float(right["times"][-1]) == new_record["last_time"], "history endpoints do not bind both checkpoint times")
        fail(all(np.array_equal(left[key], right[key][:count]) for key in HISTORY), "successor does not preserve the exact complete parent history")
    old_attestation = report_job(old_report, old.parent, old_record, old_record["output_hashes"])
    new_attestation = report_job(new_report, new.parent, new_record, new_record["output_hashes"], old_binding["sha256"])
    return dict(old=old_binding, successor=new_binding, old_verification=old_attestation,
                successor_verification=new_attestation,
                invariants={key: old_record["config"][key] for key in INVARIANTS},
                exact_parent_history_preserved=True)


@contextmanager
def retirement_lock():
    path = CAMPAIGN / ".checkpoint_retirement.lock"
    fail(not path.is_symlink(), "retirement lock is a symlink")
    with open(path, "a") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        yield


def durable_exclusive_json(path, value):
    path = path_in_campaign(path)
    payload = (json.dumps(value, indent=2, sort_keys=True, allow_nan=False) + "\n").encode()
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o444)
    try:
        with os.fdopen(descriptor, "wb", closefd=False) as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
    finally:
        os.close(descriptor)
    directory = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(directory)
    finally:
        os.close(directory)


def descriptor_path(checkpoint):
    return path_in_campaign(checkpoint).parent / "state.retirement.json"


def receipt_path(checkpoint):
    return path_in_campaign(checkpoint).parent / "state.retirement.receipt.json"


def prepare(old, new, old_report, new_report):
    with retirement_lock():
        bound = evidence(old, new, old_report, new_report)
        old, new = Path(bound["old"]["checkpoint"]), Path(bound["successor"]["checkpoint"])
        descriptor = dict(schema=SCHEMA, action="retire_only_superseded_network_state", prepared_utc=datetime.now(timezone.utc).isoformat(),
                          helper_source_sha256=sha256(__file__), **bound,
                          old_file_identity=identity(old), successor_file_identity=identity(new),
                          deletion_authorized_by_preparation=False,
                          preservation="All records, configurations, histories, dense outputs, logs, failure evidence and successor state remain.",
                          historical_limit="After retirement the old checkpoint cannot be replayed; its original bytes are attested only by retained hash evidence.")
        path = descriptor_path(old)
        durable_exclusive_json(path, descriptor)
        return dict(prepared=True, deleted=False, descriptor=str(path), descriptor_sha256=sha256(path),
                    eligible_bytes=descriptor["old_file_identity"]["size"])


def validate_descriptor(path, require_old, require_new):
    path = path_in_campaign(path)
    regular_file(path)
    descriptor = read_json(path)
    fail(descriptor.get("schema") == SCHEMA and descriptor.get("action") == "retire_only_superseded_network_state", "unsupported retirement descriptor")
    fail(path == descriptor_path(descriptor["old"]["checkpoint"]), "retirement descriptor is not stored beside its old checkpoint")
    bound = evidence(descriptor["old"]["checkpoint"], descriptor["successor"]["checkpoint"],
                     descriptor["old_verification"]["path"], descriptor["successor_verification"]["path"], require_old, require_new)
    for key, value in bound.items():
        fail(descriptor.get(key) == value, f"retirement evidence changed: {key}")
    return descriptor


def execute(path):
    with retirement_lock():
        path = path_in_campaign(path)
        initial = read_json(path)
        old = path_in_campaign(initial["old"]["checkpoint"])
        new = path_in_campaign(initial["successor"]["checkpoint"])
        already_missing = not old.exists()
        descriptor = validate_descriptor(path, require_old=not already_missing, require_new=True)
        fail(descriptor["helper_source_sha256"] == sha256(__file__), "execution helper differs from the prepared version")
        receipt = receipt_path(old)
        if receipt.exists():
            fail(already_missing, "a retirement receipt exists but the old checkpoint is present")
            return historical_evidence(old, descriptor["old"]["sha256"])
        fail(identity(new) == descriptor["successor_file_identity"], "successor checkpoint was replaced after preparation")
        if not already_missing:
            fail(identity(old) == descriptor["old_file_identity"], "old checkpoint was replaced after preparation")
        # Bind the last pre-unlink check to both checkpoint bytes and every
        # preserved evidence file; no target discovery occurs during execution.
        final = validate_descriptor(path, require_old=not already_missing, require_new=True)
        fail(final == descriptor, "descriptor changed during execution")
        fail(identity(new) == descriptor["successor_file_identity"], "successor changed during execution")
        if not already_missing:
            fail(identity(old) == descriptor["old_file_identity"], "old checkpoint changed during execution")
            # Pin the directory so an ancestor rename cannot redirect unlink.
            # Completed directory entries must still remain immutable under the
            # supervisor's ownership between this check and the unlink call.
            directory = os.open(old.parent, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
            try:
                info = os.stat(old.name, dir_fd=directory, follow_symlinks=False)
                observed = dict(device=info.st_dev, inode=info.st_ino, size=info.st_size, mtime_ns=info.st_mtime_ns)
                fail(stat.S_ISREG(info.st_mode) and info.st_nlink == 1 and observed == descriptor["old_file_identity"],
                     "pinned old checkpoint differs before unlink")
                os.unlink(old.name, dir_fd=directory)
                os.fsync(directory)
            finally:
                os.close(directory)
        fail(not old.exists(), "old checkpoint remains after requested retirement")
        receipt_value = dict(schema=SCHEMA, status="retired", descriptor=str(path), descriptor_sha256=sha256(path),
                             old_checkpoint=str(old), old_sha256=descriptor["old"]["sha256"],
                             successor_checkpoint=str(new), successor_sha256=descriptor["successor"]["sha256"],
                             observed_utc=datetime.now(timezone.utc).isoformat(), old_checkpoint_present=False,
                             deletion_performed_this_invocation=not already_missing,
                             recovered_after_prepared_checkpoint_was_missing=already_missing,
                             helper_source_sha256=sha256(__file__))
        durable_exclusive_json(receipt, receipt_value)
        return dict(retired=True, deleted_this_invocation=not already_missing, checkpoint=str(old),
                    descriptor=str(path), receipt=str(receipt), successor=str(new),
                    bytes_released=descriptor["old_file_identity"]["size"] if not already_missing else 0)


def historical_evidence(checkpoint, expected_hash, visited=None):
    checkpoint = path_in_campaign(checkpoint)
    visited = set() if visited is None else set(visited)
    fail(checkpoint not in visited, "cycle in checkpoint retirement chain")
    visited.add(checkpoint)
    fail(not checkpoint.exists(), "historical attestation is only for absent checkpoints")
    path = descriptor_path(checkpoint)
    descriptor = validate_descriptor(path, require_old=False, require_new=False)
    fail(descriptor["old"]["sha256"] == expected_hash, "historical checkpoint hash does not match requested parent")
    receipt_file = path_in_campaign(receipt_path(checkpoint))
    regular_file(receipt_file)
    receipt = read_json(receipt_file)
    fail(receipt.get("schema") == SCHEMA and receipt.get("status") == "retired"
         and receipt.get("descriptor_sha256") == sha256(path)
         and receipt.get("old_checkpoint") == str(checkpoint) and receipt.get("old_sha256") == expected_hash
         and receipt.get("old_checkpoint_present") is False, "missing or inconsistent completed retirement receipt")
    successor = path_in_campaign(descriptor["successor"]["checkpoint"])
    successor_hash = descriptor["successor"]["sha256"]
    fail(receipt.get("successor_checkpoint") == str(successor) and receipt.get("successor_sha256") == successor_hash,
         "retirement receipt successor differs")
    if successor.exists():
        regular_file(successor)
        fail(sha256(successor) == successor_hash, "terminal successor checkpoint hash differs")
        terminal, chain = str(successor), []
    else:
        next_evidence = historical_evidence(successor, successor_hash, visited)
        terminal, chain = next_evidence["live_terminal_checkpoint"], next_evidence["retirement_chain"]
    return dict(passed=True, path=str(checkpoint), expected=expected_hash, evidence_kind="historical_attestation",
                observed_live_state_hash=False, checkpoint_replayable=False,
                explanation="Checkpoint retired; original hash is supported by retained prior verification, not by a present file or fresh replay.",
                descriptor=str(path), descriptor_sha256=sha256(path), receipt=str(receipt_path(checkpoint)),
                retirement_chain=[str(path)] + chain, live_terminal_checkpoint=terminal)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--old")
    parser.add_argument("--new")
    parser.add_argument("--old-verification")
    parser.add_argument("--new-verification")
    parser.add_argument("--execute", metavar="DESCRIPTOR")
    args = parser.parse_args()
    if args.execute:
        fail(not any((args.old, args.new, args.old_verification, args.new_verification)), "execution takes only its prepared descriptor")
        result = execute(args.execute)
    else:
        fail(all((args.old, args.new, args.old_verification, args.new_verification)), "preparation requires old/new checkpoints and both verification reports")
        result = prepare(args.old, args.new, args.old_verification, args.new_verification)
    print(json.dumps(result, indent=2, allow_nan=False), flush=True)


if __name__ == "__main__":
    main()
