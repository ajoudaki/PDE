from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import centered_reference
postprocess_spec = importlib.util.spec_from_file_location(
    "campaign3_postprocess_for_results", HERE/"postprocess.py"
)
postprocess = importlib.util.module_from_spec(postprocess_spec)
assert postprocess_spec.loader is not None
postprocess_spec.loader.exec_module(postprocess)


def production() -> dict:
    return json.loads((HERE/"frozen/results_order7.json").read_text())


def test_production_matches_transparent_oracle_through_order_three():
    reference = centered_reference.run(3)
    actual = production()
    assert actual["jets_t"][:4] == [
        [str(value) for value in jet]
        for jet in reference["jets_t"]
    ]


def test_mandatory_parity_degree_and_endpoint_gates():
    jets = postprocess.load_jets(HERE/"frozen/results_order7.json")
    accepted = {1: 111, 3: 1_685_184, 5: 77_400_633_120,
                7: 7_315_868_433_079_296}
    for order, expected in accepted.items():
        assert jets[order].eval(1) == expected
        assert jets[order].degree() <= 2*(order+1)
    assert production()["jets_t"][0] == ["0"]
    assert production()["jets_t"][2] == ["0"]
    assert production()["jets_t"][4] == ["0"]
    assert production()["jets_t"][6] == ["0"]


def test_centered_endpoint_exact_values():
    jets = postprocess.load_jets(HERE/"frozen/results_order7.json")
    assert jets[1].eval(0) == 60
    assert jets[3].eval(0) == 642_048
    assert jets[5].eval(0) == 20_623_116_288
    assert jets[7].eval(0) == 1_364_310_912_663_552


def test_every_stored_interval_certificate_is_strict():
    data = json.loads((HERE/"certificates_order7.json").read_text())
    for certificate in data["certificates"].values():
        assert certificate["strictly_positive_for_c_in_0_2"]
        for half in certificate["halves"].values():
            assert half["numerator"]["strictly_positive"]
            assert half["denominator"]["strictly_positive"]
            assert half["numerator"]["real_root_count_closed_interval"] == 0
            assert half["denominator"]["real_root_count_closed_interval"] == 0
