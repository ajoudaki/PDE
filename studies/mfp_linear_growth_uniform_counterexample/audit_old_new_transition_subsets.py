"""Audit every old/new high-derivative assignment in the 979-term map."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "FULL_L2_PAIRED_ORDER5_MAP.json").read_text())


def block(atom: dict[str, object]) -> tuple[int, int, str, tuple[int, ...]]:
    exponent = tuple(atom["exponent"])
    excess = sum((order - 1) * exponent[order] for order in range(2, 6))
    factors = sum(exponent[2:])
    # This is conservative.  A lone fifth derivative becomes quadratic only
    # if a transition-dependent slope shares its source; otherwise three
    # integrations by parts give strictly positive margin.
    if (excess, factors) == (4, 1):
        factors = 2
    return excess, factors, str(atom["layer"]), exponent


def main() -> None:
    negative = []
    zero = []
    margins: Counter[tuple[int, int]] = Counter()

    for term_index, term in enumerate(DATA["paired_map"]):
        blocks = [block(atom) for atom in term["atoms"]]
        blocks = [item for item in blocks if item[0]]

        # A new insertion may occupy any nonempty subset of the high-
        # derivative atoms; all complementary atoms can be fixed old-ladder
        # moments.  The all-new census alone is therefore insufficient.
        for mask in range(1, 1 << len(blocks)):
            new = [item for index, item in enumerate(blocks) if mask & (1 << index)]
            delta_margin = 1 + sum(k + 1 - e for e, k, _layer, _exp in new)
            gamma_margin_twice = 1 + sum(3 - e for e, _k, _layer, _exp in new)
            margins[(delta_margin, gamma_margin_twice)] += 1
            record = (
                term_index,
                term["coefficient"],
                tuple(blocks),
                tuple(new),
                delta_margin,
                gamma_margin_twice,
            )
            if delta_margin < 0 or gamma_margin_twice < 0:
                negative.append(record)
            elif delta_margin == 0 and gamma_margin_twice == 0:
                zero.append(record)

    assert not negative
    assert len(zero) == 267
    assert len({record[0] for record in zero}) == 267
    assert all(
        len(record[3]) == 1 and record[3][0][:2] == (4, 2)
        for record in zero
    )

    zero_atoms = Counter((record[3][0][2], record[3][0][3]) for record in zero)
    print("old/new subset margin census", dict(sorted(margins.items())))
    print("negative-margin assignments", len(negative))
    print("zero-margin assignments", len(zero))
    print("zero-margin atom census", dict(sorted(zero_atoms.items())))


if __name__ == "__main__":
    main()
