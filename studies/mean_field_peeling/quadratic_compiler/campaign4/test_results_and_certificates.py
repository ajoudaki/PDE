from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys

import sympy as sp


HERE = Path(__file__).resolve().parent
REPOSITORY_ROOT = HERE.parents[3]
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import postprocess


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_atomic_result_manifest_and_frozen_gates():
    result_path = HERE/"results_order9.json"
    result = json.loads(result_path.read_text())
    assert result["all_diagonal_and_canonical_gates_passed"] is True
    assert result["metric"] == "D_a + alpha D_u + beta D_W"
    assert result["production"]["sector_count"] == 125
    assert result["production"]["cumulative_wall_seconds"] <= 1800
    assert result["production"]["memory_bytes_per_sector"] == 4*1024**3

    manifest = result["sector_manifest"]
    assert len(manifest) == 125
    keys = {(item["order"], item["w_hits"], item["a_hits"])
            for item in manifest}
    expected_keys = {
        (order, w_hits, a_hits)
        for order in (1, 3, 5, 7, 9)
        for w_hits in range(order+1)
        for a_hits in range(order-w_hits+1)
    }
    assert keys == expected_keys
    for item in manifest:
        path = Path(item["path"])
        if not path.is_absolute():
            path = REPOSITORY_ROOT/path
        assert path.is_file()
        assert sha256(path) == item["sha256"]

    canonical = {
        1: 111,
        3: 1_685_184,
        5: 77_400_633_120,
        7: 7_315_868_433_079_296,
        9: 1_181_161_141_825_400_561_664,
    }
    for jet in result["jets"]:
        order = int(jet["order"])
        if order % 2 == 0:
            assert jet["monomials"] == []
        else:
            assert int(jet["canonical_alpha1_beta1"]) == canonical[order]


def test_exact_certificate_replays_from_raw_jets():
    expected = json.loads((HERE/"certificates_order9.json").read_text())
    obtained = postprocess.compute(HERE/"results_order9.json")
    assert obtained == expected


def test_every_accessible_numerator_is_strictly_positive_off_origin():
    certificate = json.loads((HERE/"certificates_order9.json").read_text())
    objects = list(certificate["moment_certificates"])
    objects.extend([certificate["ordinary_H1"], certificate["shifted_H1"]])
    expected = {
        "mu_0": (3, 9),
        "mu_1": (6, 25),
        "mu_2": (9, 49),
        "mu_3": (12, 81),
        "ordinary_H1": (12, 81),
        "shifted_H1": (18, 169),
    }
    for item in objects:
        assert (item["numerator_total_degree"],
                item["numerator_term_count"]) == expected[item["name"]]
        assert all(int(term["coefficient"]) > 0
                   for term in item["numerator_coefficients"])
        assert int(item["denominator_at_origin"]) > 0
        decision = item["decision"]
        assert decision["status"] == "nonnegative_on_quadrant"
        assert decision["zero_set_on_closed_quadrant"] == (
            "union_of_strata: origin"
        )
        assert decision["strictness_by_closed_quadrant_stratum"] == {
            "origin": False,
            "positive_alpha_axis": True,
            "positive_beta_axis": True,
            "strictly_positive_interior": True,
        }


def test_shifted_determinant_restricts_to_frozen_campaign1_ray():
    certificate = json.loads((HERE/"certificates_order9.json").read_text())
    frozen = json.loads((
        HERE.parent/"campaign1/hankel_certificates_order9_q2_order8.json"
    ).read_text())
    alpha, beta, lam = sp.symbols("alpha beta lambda")
    bivariate = sp.sympify(certificate["shifted_H1"]["expression"],
                           locals={"alpha": alpha, "beta": beta})
    # ``lambda`` is a Python keyword, so rename the frozen display variable
    # before passing the exact string to SymPy's parser.
    frozen_expression = frozen["output_shifted_2x2"][
        "raw_expression"
    ].replace("lambda", "lam")
    diagonal = sp.sympify(frozen_expression, locals={"lam": lam})
    assert sp.cancel(bivariate.subs({alpha: lam, beta: lam})-diagonal) == 0
