"""Mandatory Campaign-5 two-colour regression through order five.

The accepted Campaign-2 equal-label compiler is the exact two-colour
specialization of the decorated-tree grammar from which Campaign 5 was
generalized.  This test recompiles that source, computes the common orders
1, 3, and 5, and checks every coefficient after the required 2^(k+1)
normalization.  It therefore does not substitute the rho=1 endpoint for the
independent two-colour gate.
"""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import tempfile


HERE = Path(__file__).resolve().parent
CAMPAIGN2 = HERE.parent / "campaign2"
SOURCE = HERE / "b3_connected.cpp"
ACCEPTED_RAW = CAMPAIGN2 / "frozen" / "plus_order7_raw.json"
ACCEPTED_SOURCE_SHA256 = (
    "5dd93cbc8fb97479e6c54dbc2202bfec42d0156014f5d34b4d40e77da9d6621f"
)

EXPECTED_NORMALIZED_EVEN_THETA = {
    1: [63, 20, 28],
    3: [279680, 423312, 788336, 143232, 50624],
    5: [
        3759728608,
        10667493088,
        29061262432,
        19827259136,
        12394753280,
        1426164224,
        263972352,
    ],
}


def test_exact_two_colour_equal_label_gate_through_order_five() -> None:
    import hashlib

    source_bytes = SOURCE.read_bytes()
    assert hashlib.sha256(source_bytes).hexdigest() == ACCEPTED_SOURCE_SHA256

    # Generate the internal two-colour mode mechanically from the accepted
    # three-colour source.  Arrays retain a zero third slot, while every
    # colour loop, the root average, and the colour-permutation quotient are
    # restricted to colours 0 and 1.  Assertions make the specialization
    # fail closed if the accepted source ever changes.
    source = source_bytes.decode()
    assert source.count("color < 3") == 2
    source = source.replace("color < 3", "color < 2")
    assert source.count("alpha < 3") == 3
    source = source.replace("alpha < 3", "alpha < 2")
    assert source.count("beta < 3") == 1
    source = source.replace("beta < 3", "beta < 2")
    old_permutation = (
        "std::next_permutation(permutation.begin(), permutation.end())"
    )
    assert source.count(old_permutation) == 1
    source = source.replace(
        old_permutation,
        "std::next_permutation(permutation.begin(), permutation.begin() + 2)",
    )
    root_two = (
        "      add_shift(result, recursion.value(root_for_alpha(2), k), 1);\n"
    )
    assert source.count(root_two) == 1
    source = source.replace(root_two, "")
    colors_three = r'{\"colors\":3'
    colors_two = r'{\"colors\":2'
    assert source.count(colors_three) == 1
    source = source.replace(colors_three, colors_two)
    assert source.count("divide order k by 3^(k+1)") == 1
    source = source.replace(
        "divide order k by 3^(k+1)", "divide order k by 2^(k+1)"
    )

    with tempfile.TemporaryDirectory(prefix="campaign5-b2-gate-") as folder:
        specialized = Path(folder) / "b2_specialization.cpp"
        specialized.write_text(source)
        binary = Path(folder) / "two_input_connected"
        subprocess.run(
            [
                "g++",
                "-std=c++20",
                "-O3",
                "-DNDEBUG",
                str(specialized),
                "-o",
                str(binary),
            ],
            check=True,
        )
        completed = subprocess.run(
            [str(binary), "5"],
            check=True,
            text=True,
            capture_output=True,
        )

    computed = json.loads(completed.stdout)
    accepted = json.loads(ACCEPTED_RAW.read_text())
    assert computed["colors"] == 2
    assert computed["normalization"] == "divide order k by 2^(k+1)"

    for order, expected in EXPECTED_NORMALIZED_EVEN_THETA.items():
        raw = [int(value) for value in computed["raw_rho"][order]]
        assert raw == [int(value) for value in accepted["raw_theta"][order]]
        assert all(raw[power] == 0 for power in range(1, len(raw), 2))
        divisor = 2 ** (order + 1)
        assert all(value % divisor == 0 for value in raw[::2])
        assert [value // divisor for value in raw[::2]] == expected
