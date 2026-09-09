"""Focused fail-closed tests for the freeze/evidence verifier."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

import numpy as np


AUDIT_ROOT = Path(__file__).resolve().parents[1]
SOURCE = AUDIT_ROOT / "source"
if str(SOURCE) not in sys.path:
    sys.path.insert(0, str(SOURCE))

import run_study as runner  # noqa: E402

VERIFY_PATH = AUDIT_ROOT / "protocol" / "verify_study.py"
SPEC = importlib.util.spec_from_file_location("audit_verify_study", VERIFY_PATH)
assert SPEC is not None and SPEC.loader is not None
verifier = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verifier)


class VerifierTests(unittest.TestCase):
    def _fixture(self, directory: Path):
        root = directory / "audit"
        root.mkdir()
        labels = {
            verifier.PROTOCOL_LABEL,
            *verifier.BASE_SOURCE_LABELS.values(),
            *verifier.STRUCTURAL_SOURCE_LABELS.values(),
        }
        for index, label in enumerate(sorted(labels)):
            base = root if label.startswith(("protocol/", "source/")) else directory
            path = base / label
            path.parent.mkdir(parents=True, exist_ok=True)
            if label == verifier.PROTOCOL_LABEL:
                path.write_text(
                    json.dumps(
                        {
                            "schema_version": 1,
                            "status": (
                                "preregistered_before_new_"
                                "scientific_trajectories"
                            ),
                        },
                        sort_keys=True,
                        separators=(",", ":"),
                    ),
                    encoding="utf-8",
                )
            else:
                path.write_text(f"frozen-{index}-{label}\n", encoding="utf-8")
        files = []
        tree = hashlib.sha256()
        for label in sorted(labels):
            base = root if label.startswith(("protocol/", "source/")) else directory
            path = base / label
            digest = verifier.sha256(path)
            files.append(
                {
                    "path": label,
                    "sha256": digest,
                    "size_bytes": path.stat().st_size,
                }
            )
            tree.update(label.encode())
            tree.update(b"\0")
            tree.update(digest.encode())
            tree.update(b"\0")
        hashes = {item["path"]: item["sha256"] for item in files}
        manifest = {
            "schema_version": 1,
            "status": "frozen_before_new_scientific_trajectories",
            "protocol_sha256": hashes[verifier.PROTOCOL_LABEL],
            "source_tree_sha256": tree.hexdigest(),
            "files": files,
            "environment": verifier.live_environment(),
            "scientific_evidence_count_at_freeze": 0,
            "notes": ["synthetic verifier fixture"],
        }
        seal = root / "results" / "seals" / "FROZEN_INPUTS.json"
        seal.parent.mkdir(parents=True)
        seal.write_text(
            json.dumps(manifest, sort_keys=True, separators=(",", ":")),
            encoding="utf-8",
        )
        return root, manifest, hashes, seal

    def _archive(
        self,
        path: Path,
        *,
        stage: str,
        protocol_sha256: str,
        seal_sha256: str,
        source_hashes: dict[str, str],
        environment: dict[str, str],
    ) -> None:
        arrays = {"value": np.arange(3.0)}
        provenance = {
            "schema_version": 1,
            "stage": stage,
            "sealed": True,
            "protocol_path": "protocol/preregistered_protocol.json",
            "protocol_sha256": protocol_sha256,
            "frozen_inputs_sha256": seal_sha256,
            "source_hashes": source_hashes,
            "config": {"case": "synthetic"},
            "config_sha256": runner._hash_json({"case": "synthetic"}),
            "environment": environment,
            "python_version": environment["python"],
            "platform": environment["platform"],
            "numpy_version": environment["numpy"],
            "scipy_version": environment["scipy"],
        }
        metadata = runner.build_output_metadata(
            provenance, arrays, {"semantics": "verifier unit test"}
        )
        runner.atomic_save_npz(path, arrays, metadata)

    def test_manifest_and_stage_maps_are_derived_from_frozen_paths(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            root, manifest, hashes, _ = self._fixture(workspace)
            with (
                mock.patch.object(verifier, "ROOT", root),
                mock.patch.object(verifier, "WORKSPACE", workspace),
            ):
                validated = verifier.validate_manifest(manifest)
                self.assertEqual(validated, hashes)
                common = verifier.expected_source_hashes("scaling", validated)
                structural = verifier.expected_source_hashes(
                    "generator", validated
                )
            self.assertEqual(set(common), set(verifier.BASE_SOURCE_LABELS))
            self.assertEqual(
                set(structural),
                {
                    *verifier.BASE_SOURCE_LABELS,
                    *verifier.STRUCTURAL_SOURCE_LABELS,
                },
            )
            with self.assertRaisesRegex(ValueError, "unknown scientific"):
                verifier.expected_source_hashes("invented", hashes)

    def test_tree_digest_and_duplicate_labels_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            root, manifest, _, _ = self._fixture(workspace)
            with (
                mock.patch.object(verifier, "ROOT", root),
                mock.patch.object(verifier, "WORKSPACE", workspace),
            ):
                bad_tree = {**manifest, "source_tree_sha256": "0" * 64}
                with self.assertRaisesRegex(ValueError, "tree"):
                    verifier.validate_manifest(bad_tree)
                duplicate = {
                    **manifest,
                    "files": manifest["files"] + [manifest["files"][0]],
                }
                with self.assertRaisesRegex(ValueError, "duplicate"):
                    verifier.validate_manifest(duplicate)
        with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
            verifier.strict_json_text('{"schema_version":1,"schema_version":1}')

    def test_archive_rejects_valid_hash_injected_under_extra_source_key(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            root, manifest, hashes, seal = self._fixture(workspace)
            expected = verifier.expected_source_hashes("scaling", hashes)
            poisoned = {
                **expected,
                "unrelated_frozen_file": hashes[verifier.PROTOCOL_LABEL],
            }
            archive = root / "results" / "scaling" / "poisoned.npz"
            archive.parent.mkdir(parents=True)
            self._archive(
                archive,
                stage="scaling",
                protocol_sha256=manifest["protocol_sha256"],
                seal_sha256=verifier.sha256(seal),
                source_hashes=poisoned,
                environment=manifest["environment"],
            )
            with self.assertRaisesRegex(ValueError, "not exactly"):
                verifier.verify_archive(
                    archive,
                    seal=manifest,
                    seal_sha256=verifier.sha256(seal),
                    frozen_hashes=hashes,
                )

    def test_archive_environment_must_equal_freeze(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            root, manifest, hashes, seal = self._fixture(workspace)
            expected = verifier.expected_source_hashes("tail_pde", hashes)
            bad_environment = {
                **manifest["environment"],
                "numpy": "poisoned-version",
            }
            archive = root / "results" / "tail_pde" / "bad_env.npz"
            archive.parent.mkdir(parents=True)
            self._archive(
                archive,
                stage="tail_pde",
                protocol_sha256=manifest["protocol_sha256"],
                seal_sha256=verifier.sha256(seal),
                source_hashes=expected,
                environment=bad_environment,
            )
            with self.assertRaisesRegex(ValueError, "environment"):
                verifier.verify_archive(
                    archive,
                    seal=manifest,
                    seal_sha256=verifier.sha256(seal),
                    frozen_hashes=hashes,
                )


if __name__ == "__main__":
    unittest.main()
