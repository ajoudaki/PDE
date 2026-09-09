#!/usr/bin/env python3
"""Independent coefficient-by-coefficient gates for the graded engine.

The production polynomial recurrence and this engine organize the same MFP
sum differently.  The production recurrence carries a dense polynomial in
``lambda``.  The graded engine fixes the number of middle-weight and readout
hits in advance and is run once per sector.  Agreement of every coefficient,
not merely the value at ``lambda=1``, checks the allocation of all derivative
histories to metric degree.
"""

from __future__ import annotations

from collections import defaultdict
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest


HERE = Path(__file__).resolve().parent
COMPILER = HERE.parent
SOURCE = HERE / "graded_sector.cpp"
PARENT = COMPILER / "sector_engine_checked.cpp"
EXPECTED_PARENT_SHA = (
    "1931b628b25d2a7c018bc20a06d14aee6ee86ca702d8abcbec17e1ec719be260"
)

# Frozen dense-polynomial results through the entire accepted lower stage.
# This is intentionally broader than a smoke test: every available coefficient
# through F^7 and Q2^6 is independently reconstructed from fixed-grade sectors.
EXPECTED = {
    ("f", 0): [0],
    ("f", 1): [27, 84],
    ("f", 2): [0, 0, 0],
    ("f", 3): [0, 123120, 699408, 862656],
    ("f", 4): [0, 0, 0, 0, 0],
    ("f", 5): [0, 0, 1730898720, 14214258432, 35456350464,
                25999125504],
    ("f", 6): [0, 0, 0, 0, 0, 0, 0],
    ("f", 7): [0, 0, 0, 50121723386880, 538325496778752,
                2023550608343040, 3103056989466624, 1600813615104000],
    ("q2", 0): [3],
    ("q2", 1): [0, 0],
    ("q2", 2): [0, 2916, 9456],
    ("q2", 3): [0, 0, 0, 0],
    ("q2", 4): [0, 0, 20751552, 123392448, 167175936],
    ("q2", 5): [0, 0, 0, 0, 0, 0],
    ("q2", 6): [0, 0, 0, 390147331968, 3343277514240,
                  8933475492864, 7317629343744],
}


def aggregate_sectors(binary: Path, root: str, order: int) -> list[int]:
    coefficients: defaultdict[int, int] = defaultdict(int)
    for w_hits in range(order + 1):
        for a_hits in range(order - w_hits + 1):
            completed = subprocess.run(
                [
                    str(binary), root, str(order),
                    str(w_hits), str(a_hits),
                ],
                cwd=COMPILER,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=30,
            )
            record = json.loads(completed.stdout)
            if record["parent_source_sha256"] != EXPECTED_PARENT_SHA:
                raise AssertionError("graded engine reports the wrong parent")
            if record["lambda_degree"] != order - a_hits:
                raise AssertionError("graded engine reports the wrong degree")
            coefficients[record["lambda_degree"]] += int(record["value"])
    return [coefficients[degree] for degree in range(order + 1)]


class GradedSectorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temporary = tempfile.TemporaryDirectory(prefix="campaign1-graded-")
        cls.binary = Path(cls.temporary.name) / "graded_sector"
        subprocess.run(
            [
                "g++", "-std=c++17", "-O2", "-DNDEBUG",
                str(SOURCE), "-o", str(cls.binary),
            ],
            cwd=COMPILER,
            check=True,
            timeout=60,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.temporary.cleanup()

    def test_every_lower_stage_lambda_coefficient(self) -> None:
        for (root, order), expected in EXPECTED.items():
            with self.subTest(root=root, order=order):
                self.assertEqual(
                    aggregate_sectors(self.binary, root, order), expected
                )

    def test_frozen_parent_hash(self) -> None:
        self.assertEqual(hashlib.sha256(PARENT.read_bytes()).hexdigest(),
                         EXPECTED_PARENT_SHA)

    def test_invalid_sector_is_rejected(self) -> None:
        completed = subprocess.run(
            [str(self.binary), "q2", "8", "8", "1"],
            cwd=COMPILER,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=10,
        )
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("safety caps", completed.stderr)


if __name__ == "__main__":
    unittest.main()
