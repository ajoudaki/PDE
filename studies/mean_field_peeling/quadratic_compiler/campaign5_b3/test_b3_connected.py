from __future__ import annotations

import json
from pathlib import Path
import subprocess

import pytest

import b3_reference as reference


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "b3_connected.cpp"


@pytest.fixture(scope="module")
def binary(tmp_path_factory):
    path = tmp_path_factory.mktemp("campaign5_binary") / "b3_connected"
    subprocess.run([
        "g++", "-std=c++20", "-O2", "-DNDEBUG", str(SOURCE), "-o", str(path)
    ], check=True)
    return path


def run(binary: Path, order: int) -> dict:
    completed = subprocess.run(
        [str(binary), str(order)], check=True, text=True, capture_output=True
    )
    return json.loads(completed.stdout)


def test_connected_matches_labelled_wick_through_order_three(binary):
    raw, _, _ = reference.run(3, 3)
    actual = [tuple(map(int, poly)) for poly in run(binary, 3)["raw_rho"]]
    assert actual == raw


def test_connected_first_derivative_and_canonical_endpoint(binary):
    raw = [tuple(map(int, poly)) for poly in run(binary, 3)["raw_rho"]]
    assert raw[1] == (423, 0, 240, 0, 336)
    assert sum(raw[1]) // 3**2 == 111
    assert sum(raw[3]) // 3**4 == 1_685_184


def test_invalid_orders_fail_closed(binary):
    for argument in ("-1", "6", "other"):
        completed = subprocess.run([str(binary), argument], capture_output=True)
        assert completed.returncode != 0

