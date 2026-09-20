"""Predeclared finite-budget scaling cases; no outcome-dependent geometry search."""
from copy import deepcopy
from diverse_cases import CASES_V2, validate_cases

DISCOVERY = {name: deepcopy(CASES_V2[name]) for name in
             ('quadrant_pairs', 'two_outliers_alternating')}
CONFIRMATION = {
    1: {
        'pairs_confirm1': dict(angles_degrees=[19,28,38,47,58,67,79,88],
            labels=[1,1,-1,-1,1,1,-1,-1], description='Jittered paired-sign cluster spanning69 degrees.'),
        'outliers_confirm1': dict(angles_degrees=[25,37,50,60,74,84,178,297],
            labels=[1,-1,1,-1,1,-1,1,-1], description='Shifted/jittered alternating cluster with two moved outliers.'),
        'negative_confirm1': deepcopy(CASES_V2['equal_semicircles']),
    },
    2: {
        'pairs_confirm2': dict(angles_degrees=[96,106,116,125,137,146,158,169],
            labels=[1,1,-1,-1,1,1,-1,-1], description='Rotated/jittered paired-sign cluster spanning73 degrees.'),
        'outliers_confirm2': dict(angles_degrees=[91,104,116,129,142,154,238,351],
            labels=[1,-1,1,-1,1,-1,1,-1], description='Rotated alternating cluster with two moved outliers.'),
        'negative_confirm2': dict(angles_degrees=[17,62,107,152,197,242,287,332],
            labels=[1,1,1,1,-1,-1,-1,-1], description='Rotated regular grouped-label octagon; negative control.'),
    },
}
SEEDS = {0: (20260920,7319), 1:(20260921,8521), 2:(20260922,9623)}
for cases in [DISCOVERY, *CONFIRMATION.values()]:
    validate_cases(cases)
