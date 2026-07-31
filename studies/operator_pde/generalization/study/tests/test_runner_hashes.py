from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "protocol" / "cases.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def metadata(path: Path) -> dict:
    with np.load(path, allow_pickle=False) as archive:
        return json.loads(str(archive["metadata_json"]))


class RunnerHashTests(unittest.TestCase):
    def _run(self, command: list[str]) -> None:
        env = os.environ.copy()
        env["PYTHONPATH"] = os.fspath(ROOT / "src")
        subprocess.run(
            command,
            cwd=ROOT,
            env=env,
            check=True,
            stdout=subprocess.DEVNULL,
        )

    def test_pde_scientific_hash_excludes_runtime_and_path(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            paths = []
            for directory in (base / "a", base / "b"):
                self._run(
                    [
                        sys.executable,
                        "run_pde.py",
                        "--case-registry",
                        os.fspath(REGISTRY),
                        "--case-id",
                        "B0",
                        "--quadrature",
                        "hybrid",
                        "--P",
                        "5",
                        "--N",
                        "2",
                        "--R",
                        "8",
                        "--duration",
                        "0.02",
                        "--dt",
                        "0.02",
                        "--sample-dt",
                        "0.02",
                        "--output-dir",
                        os.fspath(directory),
                    ]
                )
                paths.append(next(directory.glob("*.npz")))
            first, second = map(metadata, paths)
            self.assertEqual(
                first["scientific_config_sha256"],
                second["scientific_config_sha256"],
            )
            self.assertEqual(paths[0].name, paths[1].name)

    def test_restart_records_source_archive_content_hash(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            common = [
                sys.executable,
                "run_pde.py",
                "--case-registry",
                os.fspath(REGISTRY),
                "--case-id",
                "B0",
                "--quadrature",
                "hybrid",
                "--P",
                "5",
                "--N",
                "2",
                "--R",
                "8",
                "--duration",
                "0.02",
                "--dt",
                "0.02",
                "--sample-dt",
                "0.02",
                "--output-dir",
                os.fspath(output),
            ]
            self._run(common)
            first = next(output.glob("*.npz"))
            self._run(common + ["--restart-from", os.fspath(first)])
            second = [
                path for path in output.glob("*.npz") if path != first
            ][0]
            self.assertEqual(metadata(second)["restart_source_sha256"], sha256(first))

    def test_dense_scientific_hash_excludes_runtime_and_path(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            paths = []
            for directory in (base / "a", base / "b"):
                self._run(
                    [
                        sys.executable,
                        "run_exact_reference.py",
                        "--case-registry",
                        os.fspath(REGISTRY),
                        "--case-id",
                        "M2",
                        "--n",
                        "8",
                        "--depth",
                        "2",
                        "--seeds",
                        "2",
                        "--seed-start",
                        "777",
                        "--workers",
                        "1",
                        "--duration",
                        "0.02",
                        "--dt",
                        "0.02",
                        "--sample-dt",
                        "0.02",
                        "--output-dir",
                        os.fspath(directory),
                    ]
                )
                paths.append(next(directory.glob("*.npz")))
            first, second = map(metadata, paths)
            self.assertEqual(
                first["scientific_config_sha256"],
                second["scientific_config_sha256"],
            )
            self.assertEqual(paths[0].name, paths[1].name)


if __name__ == "__main__":
    unittest.main()
