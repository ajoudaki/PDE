from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "independent_hidden_recurrence.py"
RESULT = HERE / "INDEPENDENT_HIDDEN_RESULT.json"


def load_module():
    name = "independent_hidden_recurrence_test_target"
    specification = importlib.util.spec_from_file_location(name, SOURCE)
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    sys.modules[name] = module
    specification.loader.exec_module(module)
    return module


def test_low_order_recurrence_reproduces_all_frozen_prefixes() -> None:
    module = load_module()
    result = module.canonical_hidden_recurrence(9, 8)
    assert result.feature_derivatives == list(module.ACCEPTED_FEATURE[:10])
    assert result.q1_derivatives == list(module.ACCEPTED_Q1)
    assert result.q2_derivatives == list(module.ACCEPTED_Q2)
    assert all(result.gates.values())


def test_retained_result_is_source_bound_and_exact_through_target_orders() -> None:
    document = json.loads(RESULT.read_text())
    feature = {int(k): int(v) for k, v in document["feature_derivatives"].items()}
    q1 = {int(k): int(v) for k, v in document["q1_derivatives"].items()}
    q2 = {int(k): int(v) for k, v in document["q2_derivatives"].items()}

    assert feature[17] == 30_555_969_894_096_099_495_444_855_650_521_777_374_167_040
    assert q1[10] == 9_449_289_134_603_204_493_312
    assert q1[12] == 2_335_862_659_100_686_978_683_764_736
    assert q1[14] == 822_828_098_233_973_314_828_964_208_181_248
    assert q1[16] == 392_633_476_632_616_859_814_117_035_223_934_304_256
    assert q2[10] == 487_967_758_483_103_808_178_176
    assert q2[12] == 145_387_231_337_138_218_955_012_063_232
    assert q2[14] == 60_684_843_616_663_232_253_966_043_066_638_336
    assert q2[16] == 33_941_339_036_399_103_897_550_977_212_861_900_095_488

    assert all(feature[k] == 0 for k in range(0, 18, 2))
    assert all(q1[k] == 0 and q2[k] == 0 for k in range(1, 17, 2))
    assert q1[0] == 1
    assert all(q1[k] == 8 * feature[k - 1] for k in range(1, 17))
    assert all(document["gates"].values())

    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == document["source"][
        "sha256"
    ]
    base = HERE.parent / "canonical_high_order" / "independent_canonical_recurrence.py"
    assert hashlib.sha256(base.read_bytes()).hexdigest() == document[
        "independent_base"
    ]["sha256"]


def test_independent_source_does_not_import_production_hidden_result() -> None:
    source = SOURCE.read_text()
    assert "production_hidden" not in source.lower()
    assert "PRODUCTION_HIDDEN_RESULT" not in source
