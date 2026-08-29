from app import sum_inclusive


def test_simple_range():
    assert sum_inclusive(1, 3) == 6


def test_single_value():
    assert sum_inclusive(5, 5) == 5


def test_swapped_args():
    assert sum_inclusive(3, 1) == 6


def test_negatives():
    assert sum_inclusive(-2, 2) == 0
