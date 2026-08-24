from partial_activation_recurrence import recurrence


def test_both_square_control_through_order_thirteen() -> None:
    assert recurrence("both", 13) == [
        0,
        111,
        0,
        1_685_184,
        0,
        77_400_633_120,
        0,
        7_315_868_433_079_296,
        0,
        1_181_161_141_825_400_561_664,
        0,
        291_982_832_387_585_872_335_470_592,
        0,
        102_853_512_279_246_664_353_620_526_022_656,
    ]


def test_inner_square_control_through_order_nine() -> None:
    assert recurrence("inner", 9) == [
        0,
        10,
        0,
        2_488,
        0,
        1_807_264,
        0,
        2_811_322_240,
        0,
        7_931_589_932_800,
    ]


def test_outer_square_control_through_order_nine() -> None:
    assert recurrence("outer", 9) == [
        0,
        11,
        0,
        5_728,
        0,
        8_078_592,
        0,
        23_535_365_120,
        0,
        120_020_610_703_360,
    ]
