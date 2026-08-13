"""Exact lower-order regression for the frozen Stage-C sector compiler."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import tempfile


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "stage_c_sector.cpp"
DENSE = HERE / "frozen" / "stage_b_connected_order5.json"
EXPECTED_SOURCE_SHA256 = (
    "f1912e81b2f25bdef04bcef9c490a0975757a64deda4cb55f74c7c50abfe64ce"
)
EXPECTED_BINARY_SHA256 = (
    "59d949b0808d92b946ec55a856764f43ed4ccbcc922c5849561c9ba73e175fbf"
)


def test_order_five_w_hit_sectors_sum_to_independent_dense_result() -> None:
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == EXPECTED_SOURCE_SHA256
    with tempfile.TemporaryDirectory(prefix="campaign5-sector-gate-") as folder:
        binary = Path(folder) / "stage_c_sector"
        subprocess.run(
            ["g++", "-std=c++20", "-O3", "-DNDEBUG", str(SOURCE), "-o", str(binary)],
            check=True,
        )
        assert hashlib.sha256(binary.read_bytes()).hexdigest() == EXPECTED_BINARY_SHA256
        sectors = []
        for w_hits in range(6):
            completed = subprocess.run(
                [str(binary), "5", "--w-hits", str(w_hits)],
                check=True,
                text=True,
                capture_output=True,
            )
            record = json.loads(completed.stdout)
            assert record["w_hits"] == w_hits
            sectors.append([int(value) for value in record["raw_rho"][5]])

    width = max(map(len, sectors))
    sector_sum = [
        sum(row[power] if power < len(row) else 0 for row in sectors)
        for power in range(width)
    ]
    independent_dense = [
        int(value) for value in json.loads(DENSE.read_text())["raw_rho"][5]
    ]
    assert sector_sum == independent_dense

