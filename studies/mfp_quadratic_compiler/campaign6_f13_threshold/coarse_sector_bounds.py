#!/usr/bin/env python3
"""Candidate coarse Wick-pair-sector envelopes for the Campaign 6 D13 probe.

This is deliberately not an exact D13 enumerator.  It collapses every derivative
history to the two hit counts that determine all total Gaussian degrees, sums the
positive rewrite coefficients exactly, and then upper-bounds every terminal Wick
expectation by the number of unrestricted pairings of each Gaussian species.

The inequality behind the envelope is rigorous but expected to be loose.  The
Campaign 6 run did not complete the frozen independent-reproduction and
per-run-provenance gates, so its newly computed endpoints are retained only as
analytically justified candidates rather than protocol-accepted certificates.
Static accepted order-9 and order-11 sector rows are used for calibration, not
as a substitute for the missing independent reproduction.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
import json
from pathlib import Path


# Exact sector values P_1,...,P_{k+1} from the audited MFP compiler.
# The order-11 last three entries agree with d11_high_sectors_exact.txt.
EXACT_SECTORS = {
    9: [
        14627977297920,
        4546495309086720,
        211436756895006720,
        3490984312448606208,
        27185927724027592704,
        114581150906254331904,
        277387051973394751488,
        385587855340280672256,
        285610646257352368128,
        87101527431460847616,
    ],
    11: [
        23170716039905280,
        17433397654868459520,
        1428455842962100715520,
        40114976109177824870400,
        530996753942041626279936,
        3868170903724215843717120,
        16894189549156196962566144,
        46146109609021522448793600,
        79443613137340581848727552,
        83655641930747138444722176,
        49117046434067436406308864,
        12285503181066227920404480,
    ],
}

EXACT_TOTALS = {
    9: 1181161141825400561664,
    11: 291982832387585872335470592,
}

# Exact threshold from exact_d13_threshold.py, retained as a Fraction so that
# every comparison in this probe is exact.
THRESHOLD = Fraction(
    982497059836127136743897882036793220177491977764234839125040220839477248,
    7556538848269898446547697632297780206383,
)

# Best already certified positive retained subsum (component cap 14).
KNOWN_D13_LOWER_CAP14 = 50393647763255899049472742772736

# The exactly evaluated two-hit weighted aggregate from
# ../TWO_HIT_CHARGING_AUDIT.md.  This is not D^11 f and must not be confused
# with the raw order-11 derivative total.
TWO_HIT_WEIGHTED_AGGREGATE_ORDER11 = 13748366485300446891099172896768


def odd_double_factorial_from_even_degree(degree: int) -> int:
    """Return (degree-1)!! for an even nonnegative Gaussian degree."""
    assert degree >= 0 and degree % 2 == 0
    out = 1
    for j in range(1, degree, 2):
        out *= j
    return out


def coefficient_mass(order: int) -> dict[tuple[int, int], int]:
    """Sum positive rewrite coefficients by (a-hit count, W-hit count).

    After r derivatives and hit counts (x,z), the invariant total degrees are

        A = r+1-2x, H = r+2+x+z, E = 2(r+1-z).

    The total outgoing coefficients of all a, h, and W rewrites are A, 8H,
    and 2E respectively.  Therefore this small DP sums the coefficients of all
    labelled derivative histories without enumerating their forest shapes.
    """
    mass: dict[tuple[int, int], int] = {(0, 0): 1}
    for r in range(order):
        nxt: defaultdict[tuple[int, int], int] = defaultdict(int)
        for (x, z), coeff in mass.items():
            A = r + 1 - 2 * x
            H = r + 2 + x + z
            E = 2 * (r + 1 - z)
            assert A >= 0 and H >= 0 and E >= 0
            if A:
                nxt[(x + 1, z)] += coeff * A
            if H:
                nxt[(x, z)] += coeff * (8 * H)
            if E:
                nxt[(x, z + 1)] += coeff * (2 * E)
        mass = dict(nxt)
    return mass


def sector_envelope(order: int) -> tuple[list[int], dict]:
    """Return unrestricted-pairing caps indexed by W-Wick-pair sector P."""
    upper = [0] * (order + 1)
    mass = coefficient_mass(order)
    state_rows = []
    for (x, z), coeff in sorted(mass.items()):
        A = order + 1 - 2 * x
        H = order + 2 + x + z
        E = 2 * (order + 1 - z)
        assert A % 2 == E % 2 == 0
        wick_cap = (
            odd_double_factorial_from_even_degree(A)
            * odd_double_factorial_from_even_degree(2 * H)
            * odd_double_factorial_from_even_degree(E)
        )
        # P is the number E/2 of W Wick pairs.  It is not the number of
        # connected components: starting from one component, z W hits produce
        # c=1+z components, and P+c=order+2.
        P = order + 1 - z
        component_count = 1 + z
        contribution = coeff * wick_cap
        upper[P - 1] += contribution
        state_rows.append(
            {
                "a_hits": x,
                "w_hits": z,
                "wick_pair_sector_P": P,
                "component_count_c": component_count,
                "coefficient_mass": coeff,
                "readout_degree": A,
                "feature_half_degree": H,
                "weight_degree": E,
                "unrestricted_wick_cap": wick_cap,
                "upper_contribution": contribution,
            }
        )
    return upper, {"states": state_rows}


def main() -> None:
    result: dict[str, object] = {
        "claim_level": (
            "analytically justified candidate envelope; not protocol-accepted "
            "because frozen reproduction/provenance gates were incomplete"
        ),
        "protocol_acceptance": {
            "campaign6_certificate_accepted": False,
            "independent_D9_sector_reproduction_completed": False,
            "independent_D11_total_reproduction_completed": False,
            "durable_per_run_provenance_completed": False,
        },
        "threshold_fraction": f"{THRESHOLD.numerator}/{THRESHOLD.denominator}",
        "threshold_decimal": float(THRESHOLD),
        "orders": {},
    }

    for order in (9, 11, 13):
        upper, detail = sector_envelope(order)
        row: dict[str, object] = {
            "upper_by_wick_pair_sector_P": upper,
            "upper_total": sum(upper),
            "state_count": len(detail["states"]),
            "states": detail["states"],
        }
        if order in EXACT_SECTORS:
            exact = EXACT_SECTORS[order]
            assert len(exact) == len(upper)
            assert sum(exact) == EXACT_TOTALS[order]
            assert all(0 <= value <= cap for value, cap in zip(exact, upper))
            row.update(
                {
                    "accepted_exact_by_wick_pair_sector_P": exact,
                    "accepted_exact_total": sum(exact),
                    "static_reference_calibration_passed": True,
                    "candidate_upper_to_accepted_exact_ratio": float(
                        Fraction(sum(upper), sum(exact))
                    ),
                    "wick_pair_sector_upper_to_exact_ratio": [
                        None if value == 0 else float(Fraction(cap, value))
                        for value, cap in zip(exact, upper)
                    ],
                }
            )
        result["orders"][str(order)] = row

    d13_upper = result["orders"]["13"]["upper_total"]
    assert isinstance(d13_upper, int)
    result["d13_decision"] = {
        "known_certified_lower": KNOWN_D13_LOWER_CAP14,
        "known_lower_over_threshold": float(Fraction(KNOWN_D13_LOWER_CAP14, 1) / THRESHOLD),
        "candidate_coarse_upper": d13_upper,
        "candidate_upper_over_threshold": float(Fraction(d13_upper, 1) / THRESHOLD),
        "lower_crosses_threshold": Fraction(KNOWN_D13_LOWER_CAP14, 1) > THRESHOLD,
        "candidate_upper_is_below_threshold": Fraction(d13_upper, 1) <= THRESHOLD,
        "campaign6_interval_certificate_accepted": False,
    }

    # The previously proposed factor-nine two-generation cap.  It is retained
    # only as a sharpness target: this script does NOT certify that inequality.
    s11_weighted = TWO_HIT_WEIGHTED_AGGREGATE_ORDER11
    nine_s11 = 9 * s11_weighted
    result["unsupported_sharpness_target"] = {
        "statement": "D13 <= 9*S11_weighted_two_hit",
        "S11_weighted_two_hit": s11_weighted,
        "nine_S11": nine_s11,
        "nine_S11_over_threshold": float(Fraction(nine_s11, 1) / THRESHOLD),
        "certified": False,
        "warning": "Known local charging variants of this inequality are false.",
    }

    out = Path(__file__).with_name("coarse_sector_bounds.json")
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(f"wrote {out}")
    print(json.dumps({
        "d9_static_calibration": result["orders"]["9"]["static_reference_calibration_passed"],
        "d11_static_calibration": result["orders"]["11"]["static_reference_calibration_passed"],
        "d9_candidate_upper_ratio": result["orders"]["9"]["candidate_upper_to_accepted_exact_ratio"],
        "d11_candidate_upper_ratio": result["orders"]["11"]["candidate_upper_to_accepted_exact_ratio"],
        "d13_candidate_upper_over_threshold": result["d13_decision"]["candidate_upper_over_threshold"],
        "known_lower_over_threshold": result["d13_decision"]["known_lower_over_threshold"],
    }, indent=2))


if __name__ == "__main__":
    main()
