"""Twelve deterministic eight-point circle cases, fixed without training results.

Angles describe the normalized direction (cos(theta), sin(theta)); the canonical
input is sqrt(2) times that direction. All cases have four labels of each sign.
The bias-free tanh network is odd, so exact antipodes must have opposite labels.
In particular, fully alternating labels on eight equally spaced points are
incompatible with this model; ``equal_mixed_odd`` is an admissible mixed pattern.

The first three cases hold geometry fixed while changing label ordering. Other
cases vary angular coverage, spacing, cluster count, and outlier count. These
are qualitative stress cases, not a random sample or a performance-selected set.
No claim that every case reaches the fitting threshold is implied.
"""

import json
import math


CASES_V2 = {
    "quadrant_grouped": {
        "angles_degrees": [10, 20, 30, 40, 50, 60, 70, 80],
        "labels": [1, 1, 1, 1, -1, -1, -1, -1],
        "description": "Eight points in a 70-degree quadrant arc; four positive then four negative labels.",
    },
    "quadrant_alternating": {
        "angles_degrees": [10, 20, 30, 40, 50, 60, 70, 80],
        "labels": [1, -1, 1, -1, 1, -1, 1, -1],
        "description": "The same 70-degree quadrant arc, with alternating labels at every point.",
    },
    "quadrant_pairs": {
        "angles_degrees": [10, 20, 30, 40, 50, 60, 70, 80],
        "labels": [1, 1, -1, -1, 1, 1, -1, -1],
        "description": "The same 70-degree quadrant arc, with alternating same-sign pairs.",
    },
    "quadrant_center_edges": {
        "angles_degrees": [15, 21, 27, 33, 39, 45, 53, 60],
        "labels": [-1, -1, 1, 1, 1, 1, -1, -1],
        "description": "A narrower 45-degree quadrant arc; four central positives and two negatives at each edge.",
    },
    "equal_semicircles": {
        "angles_degrees": [0, 45, 90, 135, 180, 225, 270, 315],
        "labels": [1, 1, 1, 1, -1, -1, -1, -1],
        "description": "Eight exactly equally spaced points; one positive and one negative semicircle, with opposite antipodal labels.",
    },
    "equal_mixed_odd": {
        "angles_degrees": [0, 45, 90, 135, 180, 225, 270, 315],
        "labels": [1, 1, -1, 1, -1, -1, 1, -1],
        "description": "The same equal spacing; neighboring positive and negative pairs plus isolated signs, preserving opposite antipodal labels.",
    },
    "near_equal_grouped": {
        "angles_degrees": [8, 48, 96, 142, 187, 230, 281, 322],
        "labels": [1, 1, 1, 1, -1, -1, -1, -1],
        "description": "Near-equal 40-to-51-degree circular gaps; four consecutive positives followed by four negatives.",
    },
    "two_clusters_grouped": {
        "angles_degrees": [10, 22, 34, 46, 125, 137, 149, 161],
        "labels": [1, 1, 1, 1, -1, -1, -1, -1],
        "description": "Two separated 36-degree clusters of four points; one positive cluster and one negative cluster.",
    },
    "two_clusters_split": {
        "angles_degrees": [10, 22, 34, 46, 125, 137, 149, 161],
        "labels": [1, 1, -1, -1, 1, 1, -1, -1],
        "description": "The same two clusters, each split into a positive pair followed by a negative pair.",
    },
    "three_clusters_mixed": {
        "angles_degrees": [15, 27, 39, 140, 152, 263, 275, 287],
        "labels": [1, 1, 1, -1, -1, 1, -1, -1],
        "description": "Three clusters of sizes three, two, and three around the circle; positive, negative, and mixed labels respectively.",
    },
    "one_outlier_grouped": {
        "angles_degrees": [12, 22, 32, 42, 52, 62, 72, 225],
        "labels": [1, 1, 1, 1, -1, -1, -1, -1],
        "description": "Seven points in a 60-degree arc with grouped labels, plus one remote negative outlier.",
    },
    "two_outliers_alternating": {
        "angles_degrees": [15, 27, 39, 51, 63, 75, 165, 285],
        "labels": [1, -1, 1, -1, 1, -1, 1, -1],
        "description": "Six alternating points in a 60-degree arc, plus two remote outliers of opposite signs.",
    },
}


def validate_cases(cases=CASES_V2):
    """Reject invalid inputs and return geometry-only diagnostics for each case.

    Coincidence and antipodality are checked modulo 360 degrees with an absolute
    tolerance of 1e-10 degrees. This is an input consistency check, not a
    representability or optimization guarantee.
    """
    diagnostics = {}
    tolerance = 1e-10
    for name, case in cases.items():
        angles, labels = case["angles_degrees"], case["labels"]
        if len(angles) != 8 or len(labels) != 8:
            raise ValueError(f"{name}: exactly eight angles and labels are required")
        if not all(math.isfinite(angle) for angle in angles):
            raise ValueError(f"{name}: angles must be finite")
        if any(isinstance(label, bool) or label not in (-1, 1) for label in labels):
            raise ValueError(f"{name}: labels must be -1 or +1")
        if not isinstance(case["description"], str) or not case["description"].strip():
            raise ValueError(f"{name}: a nonempty description is required")
        normalized = [angle % 360 for angle in angles]
        antipodal_pairs = []
        for i in range(8):
            for j in range(i + 1, 8):
                difference = abs(normalized[i] - normalized[j])
                distance = min(difference, 360 - difference)
                if distance <= tolerance:
                    raise ValueError(f"{name}: angles {i} and {j} coincide modulo 360")
                if abs(distance - 180) <= tolerance:
                    if labels[i] != -labels[j]:
                        raise ValueError(f"{name}: antipodal labels {i} and {j} contradict oddness")
                    antipodal_pairs.append([i, j])
        ordered = sorted(normalized)
        gaps = [ordered[i + 1] - ordered[i] for i in range(7)]
        gaps.append(360 + ordered[0] - ordered[-1])
        diagnostics[name] = {
            "points": 8,
            "positive_labels": labels.count(1),
            "negative_labels": labels.count(-1),
            "minimum_gap_degrees": min(gaps),
            "maximum_gap_degrees": max(gaps),
            "covering_arc_degrees": 360 - max(gaps),
            "antipodal_pairs": antipodal_pairs,
        }
    return diagnostics


if __name__ == "__main__":
    print(json.dumps(validate_cases(), indent=2, allow_nan=False))
