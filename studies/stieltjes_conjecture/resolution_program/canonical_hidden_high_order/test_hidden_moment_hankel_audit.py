"""Regression tests for the exact hidden-norm downstream audit."""

import json
from fractions import Fraction

import hidden_moment_hankel_audit as audit


Q = Fraction
FEATURE = {
    0: 0,
    1: 111,
    2: 0,
    3: 1_685_184,
    4: 0,
    5: 77_400_633_120,
    6: 0,
    7: 7_315_868_433_079_296,
    8: 0,
    9: 1_181_161_141_825_400_561_664,
    10: 0,
    11: 291_982_832_387_585_872_335_470_592,
    12: 0,
    13: 102_853_512_279_246_664_353_620_526_022_656,
    14: 0,
    15: 49_079_184_579_077_107_476_764_629_402_991_788_032,
    16: 0,
    17: 30_555_969_894_096_099_495_444_855_650_521_777_374_167_040,
}
EXPECTED_Q1 = (
    Q(4, 111),
    Q(561_728, 50_602_347),
    Q(1_100_387_825_680, 207_616_015_289_871),
    Q(477_889_187_282_572_736, 157_745_610_337_167_536_445),
    Q(
        14_424_778_706_424_668_415_965_888,
        7_550_822_538_386_077_126_253_412_825,
    ),
    Q(
        119_118_565_349_315_704_829_440_551_507_968,
        92_940_650_810_959_401_416_295_731_117_408_175,
    ),
    Q(
        139_410_823_899_678_072_727_103_593_176_995_378_368,
        155_354_851_922_408_376_478_007_713_053_572_517_513_075,
    ),
    Q(
        1_139_365_750_155_201_547_146_390_268_983_992_991_479_348_176,
        1_757_690_740_504_006_492_738_224_469_237_864_513_509_282_641_325,
    ),
    Q(
        81_513_106_935_036_070_336_834_887_802_279_846_324_127_484_536_014_984,
        169_988_115_833_926_611_045_240_711_599_811_955_975_032_970_768_397_968_875,
    ),
)


def test_series_inverse_and_square_root_identities() -> None:
    feature = [Q(0), Q(2), Q(0), Q(3)]
    inverse = audit.direct_inverse(feature, 3)
    assert audit.compose_series(feature, inverse, 3) == [Q(0), Q(1), Q(0), Q(0)]
    root = audit.sqrt_unit_series((Q(1), Q(2), Q(5), Q(4)))
    assert audit.multiply_series(root, root, 3) == [Q(1), Q(2), Q(5), Q(4)]


def test_first_hidden_ward_sequence_through_ninth_moment() -> None:
    # Q2 is immaterial to this assertion but response_moments validates both
    # observables, so use the retained independent exact jet as its input.
    document = json.loads(audit.INDEPENDENT_RESULT.read_text())
    q2 = audit.exact_derivatives(document, "q2_derivatives")
    sequences = audit.response_moments(FEATURE, q2)
    assert sequences["first_hidden_squared_rms"] == EXPECTED_Q1
    gates = audit.all_hankel_gates(EXPECTED_Q1)
    assert gates["ordinary_H4"]["positive_definite"]
    assert gates["shifted_H3"]["positive_definite"]


def test_retained_cross_implementation_audit() -> None:
    result = audit.build_audit(audit.PRODUCTION_RESULT, audit.INDEPENDENT_RESULT)
    sequences = result["sequences"]
    expected_existing_q2 = (
        "2062/4107",
        "678331568/5616860517",
        "2090752728035608/38408962828626135",
        "137586915791251406192/4539568119702932437695",
    )
    assert tuple(
        sequences["second_hidden_squared_rms"]["moments"][:4]
    ) == expected_existing_q2
    assert all(
        sequence["all_accessible_principal_minors_strictly_positive"]
        for sequence in sequences.values()
    )
