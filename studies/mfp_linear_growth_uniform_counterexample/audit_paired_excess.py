"""Hostile census for the excess claim in FULL_L2_LIPSCHITZ_LADDER.md."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
from fractions import Fraction


HERE = Path(__file__).resolve().parent
try:
    from .map_inputs import load_map, parse_map_path
except ImportError:
    from map_inputs import load_map, parse_map_path


def block(atom: dict[str, object]) -> tuple[int, int]:
    exponent = atom["exponent"]
    assert isinstance(exponent, list)
    excess = sum((order - 1) * count for order, count in enumerate(exponent) if order >= 2)
    factors = sum(count for order, count in enumerate(exponent) if order >= 2)
    return excess, factors


def main() -> None:
    DATA = load_map(parse_map_path())
    census: Counter[int] = Counter()
    max_atom_excess = 0
    two_principal_blocks = []
    zero_margin_multiblocks = []
    lower_principal = Fraction(0)
    lower_principal_indices = []

    for index, term in enumerate(DATA["paired_map"]):
        blocks = []
        for atom in term["atoms"]:
            excess, factors = block(atom)
            max_atom_excess = max(max_atom_excess, excess)
            if excess:
                blocks.append((excess, factors, atom["layer"], tuple(atom["exponent"])))

        total_excess = sum(item[0] for item in blocks)
        census[total_excess] += 1

        principal = [item for item in blocks if item[0] == 4 and item[1] >= 2]
        if len(principal) >= 2:
            two_principal_blocks.append((index, term["coefficient"], blocks))

        # Under w=delta*sqrt(gamma), an atom with (e,k) scales as
        # delta^(k+1-e) gamma^((3-e)/2).  Divide a product by the
        # principal delta^(-1) gamma^(-1/2) scale.
        if blocks and not any(e == 4 and k == 1 for e, k, *_ in blocks):
            delta_margin = 1 + sum(k + 1 - e for e, k, *_ in blocks)
            gamma_margin_twice = 1 + sum(3 - e for e, _k, *_ in blocks)
            if delta_margin == 0 and gamma_margin_twice == 0 and len(blocks) > 1:
                zero_margin_multiblocks.append((index, term["coefficient"], blocks))

        # In the lower-source principal sector the only allowed companion
        # atoms are three top-layer E[psi'(G)^2] atoms.  Integrating the
        # transition gives +I for (psi''')^2, -I for psi'' psi'''', and
        # nu_1*I for the first slope variation next to psi^(5).
        high_atoms = [
            atom for atom in term["atoms"] if block(atom)[0]
        ]
        if len(high_atoms) == 1 and high_atoms[0]["layer"] == "X":
            atom = high_atoms[0]
            exponent = atom["exponent"]
            excess, factors = block(atom)
            multiplier = Fraction(0)
            if excess == 4 and factors == 2 and exponent[3] == 2:
                multiplier = Fraction(1)
            elif excess == 4 and factors == 2 and exponent[2] == exponent[4] == 1:
                multiplier = Fraction(-1)
            elif excess == 4 and factors == 1 and exponent[5] == 1:
                multiplier = Fraction(exponent[1])

            companions = [other for other in term["atoms"] if other is not atom]
            expected = [0, 2, 0, 0, 0, 0]
            if multiplier and len(companions) == 3 and all(
                other["layer"] == "Y" and other["exponent"] == expected
                for other in companions
            ):
                lower_principal += Fraction(term["coefficient"]) * multiplier
                lower_principal_indices.append(index)

    assert len(DATA["paired_map"]) == 979
    assert dict(sorted(census.items())) == {
        0: 6,
        1: 24,
        2: 86,
        3: 126,
        4: 244,
        5: 198,
        6: 186,
        7: 73,
        8: 36,
    }
    assert max_atom_excess == 4
    assert not two_principal_blocks
    assert not zero_margin_multiblocks
    assert lower_principal_indices == [685, 686, 691]
    assert lower_principal == Fraction(-55, 8)

    print("monomials", len(DATA["paired_map"]))
    print("total-excess census", dict(sorted(census.items())))
    print("maximum individual-atom excess", max_atom_excess)
    print("terms with two principal blocks", len(two_principal_blocks))
    print("zero-margin multiblock terms", len(zero_margin_multiblocks))
    print("lower principal indices", lower_principal_indices)
    print("lower principal coefficient", lower_principal)


if __name__ == "__main__":
    main()
