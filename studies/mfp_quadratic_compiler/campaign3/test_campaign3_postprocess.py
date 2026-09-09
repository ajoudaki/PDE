from __future__ import annotations

import importlib.util
from pathlib import Path
import sympy as sp


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "campaign3_postprocess_module", HERE/"postprocess.py"
)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)
t = module.t


def test_universal_reversion_matches_canonical_moments():
    jets = {
        1: sp.Poly(111, t),
        3: sp.Poly(1_685_184, t),
        5: sp.Poly(77_400_633_120, t),
        7: sp.Poly(7_315_868_433_079_296, t),
    }
    values = module.stieltjes_expressions(jets)
    assert values["mu0"] == sp.Rational(280864, 4107)
    assert values["mu1"] == sp.Rational(38443196932, 5616860517)
    assert values["mu2"] == sp.Rational(
        37578479127292096, 12802987609542045
    )


def test_sturm_positive_polynomial_both_halves():
    polynomial = sp.Poly(3+2*t+5*t**2, t)
    assert module.strict_polynomial_certificate(polynomial, -1, 0)[
        "strictly_positive"
    ]
    assert module.strict_polynomial_certificate(polynomial, 0, 1)[
        "strictly_positive"
    ]
