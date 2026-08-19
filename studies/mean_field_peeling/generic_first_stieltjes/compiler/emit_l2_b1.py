"""Emit the two-hidden-layer, one-input GNF as literal LaTeX or JSON."""

from __future__ import annotations

import argparse
import json

from .l2_b1_correction import first_correction_normal_form
from .normal_form import (
    add,
    atom_inventory,
    maximum_activation_derivative,
    to_data,
    to_latex,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--format", choices=("json", "latex", "summary"), default="summary")
    args = parser.parse_args()

    state = first_correction_normal_form()
    inventory = atom_inventory(add(state.ntk, state.correction))
    if args.format == "latex":
        print("A=" + to_latex(state.ntk))
        print("C=" + to_latex(state.correction))
        return
    if args.format == "json":
        print(
            json.dumps(
                {
                    "model": "L=2 hidden layers, B=1, raw-coordinate muP",
                    "A": to_data(state.ntk),
                    "C": to_data(state.correction),
                    "atoms": [to_data(item) for item in inventory],
                    "atom_count": len(inventory),
                    "maximum_activation_derivative": maximum_activation_derivative(
                        state.correction
                    ),
                },
                indent=2,
                sort_keys=True,
            )
        )
        return
    print("model: L=2 hidden layers, B=1, raw-coordinate muP")
    print(f"unique Gaussian atoms for (A,C): {len(inventory)}")
    print(
        "maximum activation derivative in C: "
        f"{maximum_activation_derivative(state.correction)}"
    )
    for index, item in enumerate(inventory, 1):
        print(f"atom[{index:02d}] {item.tag}: {to_latex(item)}")


if __name__ == "__main__":
    main()
