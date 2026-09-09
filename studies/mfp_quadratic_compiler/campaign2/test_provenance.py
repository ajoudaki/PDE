#!/usr/bin/env python3

import hashlib
import json
from pathlib import Path
import unittest


HERE = Path(__file__).resolve().parent


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class ProvenanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((HERE / "provenance_order7.json").read_text())

    def test_durable_hashes(self):
        mapping = {
            "source_sha256": HERE / "two_input_connected.cpp",
            "reference_source_sha256": HERE / "two_input_reference.py",
            "postprocess_source_sha256": HERE / "postprocess.py",
            "certificates_sha256": HERE / "certificates_order7.json",
        }
        for field, path in mapping.items():
            self.assertEqual(self.data[field], sha256(path), field)
        route = self.data["amended_accelerated_route"]
        self.assertEqual(
            route["plus"]["raw_sha256"],
            sha256(HERE / "frozen/plus_order7_raw.json"),
        )
        self.assertEqual(
            route["minus"]["raw_sha256"],
            sha256(HERE / "frozen/minus_order7_raw.json"),
        )

    def test_local_binary_when_present(self):
        binary = HERE / "frozen/two_input_connected_vp"
        if binary.exists():
            self.assertEqual(self.data["frozen_binary_sha256"], sha256(binary))

    def test_status_and_caps(self):
        failed = self.data["original_dense_attempt"]
        self.assertEqual(failed["exit_status"], 124)
        self.assertEqual(failed["status"], "inconclusive_timeout")
        self.assertIsNone(failed["source_sha256"])
        self.assertTrue(failed["provenance_limitation"])
        amended = self.data["amended_accelerated_route"]
        self.assertEqual(amended["resource_cap_per_channel"]["wall_seconds"],
                         1200)
        self.assertEqual(
            amended["resource_cap_per_channel"]["virtual_memory_kib"],
            4194304,
        )
        self.assertEqual(amended["plus"]["exit_status"], 0)
        self.assertEqual(amended["minus"]["exit_status"], 0)
        self.assertTrue(
            self.data["validation"]["all_17_unit_tests_pass"]
        )

    def test_logs_exist(self):
        paths = [self.data["original_dense_attempt"]["log"]]
        route = self.data["amended_accelerated_route"]
        paths.extend((route["plus"]["log"], route["minus"]["log"]))
        for path in paths:
            self.assertTrue((HERE / path).is_file(), path)


if __name__ == "__main__":
    unittest.main()
