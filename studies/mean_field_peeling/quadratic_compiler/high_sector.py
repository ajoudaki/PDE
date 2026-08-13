#!/usr/bin/env python3
"""Generate/evaluate only the q=1,2 (maximal Wick-pair) sectors."""

from __future__ import annotations

import argparse
import json
import pickle
from pathlib import Path

import exact_graph_wick as eg


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--order", type=int, default=11)
    ap.add_argument("--checkpoint", type=Path, required=True)
    ap.add_argument("--resume", action="store_true")
    ap.add_argument("--evaluate", action="store_true")
    args = ap.parse_args()

    if args.resume and args.checkpoint.exists():
        with args.checkpoint.open("rb") as f:
            state = pickle.load(f)
        order, poly = state["order"], state["poly"]
    else:
        order, poly = 0, eg.initial_observable()

    while order < args.order:
        poly = {key: value for key, value in eg.differentiate(poly).items() if key[0] <= 2}
        order += 1
        with args.checkpoint.open("wb") as f:
            pickle.dump({"order": order, "poly": poly}, f, protocol=5)
        print(json.dumps({
            "order": order,
            "q1_graphs": sum(q == 1 for q, _ in poly),
            "q2_graphs": sum(q == 2 for q, _ in poly),
        }), flush=True)

    if args.evaluate:
        for q in (1, 2):
            sector = {key: value for key, value in poly.items() if key[0] == q}
            print(json.dumps({
                "order": order,
                "q": q,
                "wick_pairs": order + 2 - q,
                "graphs": len(sector),
                "derivative_contribution": str(eg.expected_large_n(sector)),
            }), flush=True)


if __name__ == "__main__":
    main()
