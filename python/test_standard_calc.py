from standard_calc import bound_to_180, is_angle_between, bound_to_0_to_360


""" Tests for bound_to_180() """


def test_bound_basic1():
    assert bound_to_180(0) == 0


def test_bound_edge_case():
    assert bound_to_180(180) == 180
    assert bound_to_180(-180) == -180


def test_bound_positive_angle_less_than_180():
    assert bound_to_180(110) == 110


def test_bound_positive_angle_greater_than_180():
    assert bound_to_180(220) == -140
    assert bound_to_180(380) == 20


def test_bound_negative_angle_greater_than_negative_180():
    assert bound_to_180(-90) == -90


def test_bound_negative_angle_less_than_negative_180():
    assert bound_to_180(-220) == 140
    assert bound_to_180(-380) == -20


""" Tests for bound_to_0_to_360() """


def test_bound_to_0_to_360_Case1():
    assert bound_to_0_to_360(200) == 200


def test_bound_to_0_to_360_Case2():
    assert bound_to_0_to_360(0) == 0


def test_bound_to_0_to_360_Case3():
    assert bound_to_0_to_360(540) == 180


def test_bound_to_0_to_360_Case4():
    assert bound_to_0_to_360(-180) == 180


def test_bound_to_0_to_360_Case5():
    assert bound_to_0_to_360(-500) == 220


""" Tests for is_angle_between() """


def test_between_basic1():
    assert is_angle_between(0, 1, 2)


def test_between_basic2():
    assert not is_angle_between(40, 80, 300)


def test_between_basic3():
    assert is_angle_between(20, 60, 200)


def test_between_basic4():
    assert is_angle_between(20, 30, 150)
