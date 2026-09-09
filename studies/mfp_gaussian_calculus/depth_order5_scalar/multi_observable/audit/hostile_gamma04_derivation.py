"""Independent hostile Gamma_04 contraction, frozen before producer inspection.

This route reuses only the *pre-existing frozen order-five* local Wick--Stein
engine.  It does not import either new Gamma_04 producer table.  The Bell
polynomial and the two response channels below were independently reconstructed
from the feature-ascent parameter ODE.
"""

from __future__ import annotations

import json

from studies.mean_field_peeling.generic_first_stieltjes.depth_order5_scalar.independent import (
    moving_contraction as m,
)


def transitions():
    gamma04 = m.sv("gamma04")
    l41, l43 = m.sv("l41"), m.sv("l43")

    old_forward_covariance = m.forward_covariance

    def forward_covariance(i: int, j: int):
        if i > j:
            i, j = j, i
        if (i, j) == (0, 4):
            return gamma04
        return old_forward_covariance(i, j)

    # The imported evaluator consults this module global.  Restore it before
    # returning so importing this hostile checker cannot alter another audit.
    m.forward_covariance = forward_covariance
    m.wick_stein.cache_clear()
    try:
        lower = m.local_polynomials()
        p = [m.rg("p", i) for i in range(6)]
        f1, g2, g3, g4 = (m.rg("f", i) for i in range(1, 5))
        e0 = m.rg("e", 0)

        d0 = m.rm(p[1], e0)
        z1 = m.ra(f1, m.rm(m.r_from_scalar(m.L1), d0))
        z2 = m.ra(g2, m.rm(m.r_from_scalar(m.L2), lower["d1"]))
        z3 = m.ra(
            g3,
            m.rm(m.r_from_scalar(m.L30), d0),
            m.rm(m.r_from_scalar(m.L32), lower["d2m"]),
        )
        z4 = m.ra(
            g4,
            m.rm(m.r_from_scalar(l41), lower["d1"]),
            m.rm(m.r_from_scalar(l43), lower["d3m"]),
        )

        x4 = m.ra(
            m.rproduct(p[4], z1, z1, z1, z1),
            m.rs(m.rproduct(p[3], z1, z1, z2), 6),
            m.rs(m.rproduct(p[2], z2, z2), 3),
            m.rs(m.rproduct(p[2], z1, z3), 4),
            m.rm(p[1], z4),
        )

        return {
            "gamma04_next": m.expectation(m.rm(lower["x0"], x4)),
            "a41_next": m.expectation(m.r_derivative(x4, "e", 1)),
            "a43_next": m.expectation(m.r_derivative(x4, "e", 4)),
        }
    finally:
        m.forward_covariance = old_forward_covariance
        m.wick_stein.cache_clear()


def formatted():
    return {name: m.format_poly(poly) for name, poly in transitions().items()}


def candidate_schedule():
    return {
        "initial": {"gamma04": "0", "a41": "0", "a43": "0"},
        "substitutions": {
            "l41": "9*q02 + 8*w + a41",
            "l43": "1 + a43",
        },
        "transition": formatted(),
    }


if __name__ == "__main__":
    print(json.dumps(candidate_schedule(), indent=2, sort_keys=True))

