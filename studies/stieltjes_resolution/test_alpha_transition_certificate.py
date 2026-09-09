import json
from fractions import Fraction

import alpha_transition_certificate as certificate


def test_unique_transition_and_classification() -> None:
    record = certificate.build_certificate()
    transition = record["unique_positive_transition"]
    assert Fraction(transition["lower_bound"]) == certificate.ROOT_LOWER
    assert Fraction(transition["upper_bound"]) == certificate.ROOT_UPPER
    assert certificate.ROOT_LOWER < certificate.ROOT_UPPER
    assert record["leading_gate_records"]["H_plus_2_det"][
        "positive_root_count"
    ] == 1


def test_every_preceding_gate_is_coefficientwise_positive() -> None:
    records = certificate.build_certificate()["leading_gate_records"]
    assert all(
        record["all_primitive_coefficients_strictly_positive"]
        for name, record in records.items()
        if name != "H_plus_2_det"
    )


def test_retained_certificate_regenerates_exactly() -> None:
    retained = json.loads(
        (certificate.HERE / "ALPHA_TRANSITION_CERTIFICATE.json").read_text()
    )
    assert certificate.build_certificate() == retained
