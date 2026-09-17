#!/usr/bin/env python3
"""Run frozen VERIFY with one explicit, exact historical README substitution.

No training is performed. All VERIFY checks remain active. The sole permitted
substitution is this study's README.md at its original frozen hash, read from
the exact regular-file archive DESIGN_PROPOSAL.md after README.md is updated.
"""
import argparse
import json
import os
from pathlib import Path
import stat
import sys

HERE = Path(__file__).resolve().parent
README = HERE / "README.md"
ARCHIVE = HERE / "DESIGN_PROPOSAL.md"
EXPECTED = "768355843fab3369f96338fccc692c7d8cae6523bc1c69bcd5fb9352290c893b"
sys.path.insert(0, str(HERE))
import VERIFY


def validate_archive():
    information = ARCHIVE.lstat()
    if (ARCHIVE.parent != HERE or ARCHIVE.name != "DESIGN_PROPOSAL.md"
            or not stat.S_ISREG(information.st_mode) or information.st_uid != os.getuid()
            or ARCHIVE.resolve() != ARCHIVE):
        raise ValueError("README archive must be this study's own regular DESIGN_PROPOSAL.md")
    actual = VERIFY.sha256(ARCHIVE)
    if actual != EXPECTED:
        raise ValueError("historical README archive differs from its exact frozen hash")
    return actual


def archive_checker(original, substitutions):
    def check(path, expected, failures, label):
        # Exact path equality: aliases and every other source use the original
        # checker. No general manifest hash or path rewriting is available.
        if Path(path) != README:
            return original(path, expected, failures, label)
        if expected != EXPECTED:
            failures.append(f"{label}: unexpected frozen README hash; substitution forbidden")
            return dict(path=str(path), expected=expected, passed=False,
                        error="unexpected frozen README hash")
        current = VERIFY.sha256(README)
        if current == EXPECTED:
            return original(path, expected, failures, label)
        archive_hash = validate_archive()
        result = original(ARCHIVE, expected, failures, label)
        result.update(original_path=str(README), archived_path=str(ARCHIVE),
                      archived_sha256=archive_hash, current_readme_sha256=current,
                      explicit_archive_substitution=True)
        substitutions.append(dict(result))
        return result
    return check


def verify(manifest, replay="none", device="cpu"):
    archive_hash = validate_archive()
    current_hash = VERIFY.sha256(README)
    original = VERIFY.check_hash
    substitutions = []
    try:
        VERIFY.check_hash = archive_checker(original, substitutions)
        result = VERIFY.verify(manifest, replay, device)
    finally:
        VERIFY.check_hash = original
    result["readme_archive"] = dict(original_path=str(README), archived_path=str(ARCHIVE),
                                    expected_frozen_sha256=EXPECTED, archived_sha256=archive_hash,
                                    current_readme_sha256=current_hash,
                                    substitution_applied=bool(substitutions), checks=substitutions)
    result["replay_wrapper_source_sha256"] = VERIFY.sha256(__file__)
    result["replay_wrapper_command"] = [sys.executable, *sys.argv]
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--replay", choices=("none", "main", "all"), default="none")
    parser.add_argument("--device", default="cpu")
    args = parser.parse_args()
    out = VERIFY.owned(args.out)
    if out.exists():
        raise ValueError("verification output must be fresh")
    result = verify(args.manifest, args.replay, args.device)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("x") as handle:
        json.dump(result, handle, indent=2, sort_keys=True, allow_nan=False)
        handle.write("\n")
    print(json.dumps(dict(passed=result["passed"], failures=result["failures"], out=str(out),
                          archive_substitution=result["readme_archive"]["substitution_applied"])), flush=True)
    return 0 if result["passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
