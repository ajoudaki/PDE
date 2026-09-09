#!/usr/bin/env python3

import json
from pathlib import Path
import subprocess
import tempfile
import unittest

import two_input_reference as reference


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "two_input_connected.cpp"


class ConnectedCompilerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.directory = tempfile.TemporaryDirectory()
        cls.binary = Path(cls.directory.name) / "compiler"
        subprocess.run(
            ["g++", "-std=c++20", "-O2", "-DNDEBUG", str(SOURCE),
             "-o", str(cls.binary)],
            check=True,
        )

    @classmethod
    def tearDownClass(cls):
        cls.directory.cleanup()

    def run_compiler(self, channel, order=3):
        result = subprocess.run(
            [str(self.binary), channel, str(order)],
            text=True,
            capture_output=True,
            check=True,
        )
        return json.loads(result.stdout)

    def test_independent_reference_agreement(self):
        for sigma, channel in ((1, "plus"), (-1, "minus")):
            expected_raw, _ = reference.run(sigma, 3)
            actual = self.run_compiler(channel)["raw_theta"]
            actual = [tuple(map(int, p)) for p in actual]
            self.assertEqual(actual, expected_raw)

    def test_normalization_and_first_derivative(self):
        for channel, expected in (
            ("plus", (63, 0, 20, 0, 28)),
            ("minus", (48, 0, -20, 0, -28)),
        ):
            raw = self.run_compiler(channel)["raw_theta"]
            desired = tuple(int(x) // 4 for x in raw[1])
            self.assertEqual(desired, expected)

    def test_invalid_requests_fail_closed(self):
        for arguments in (("other", "3"), ("plus", "9")):
            result = subprocess.run(
                [str(self.binary), *arguments], capture_output=True
            )
            self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()

