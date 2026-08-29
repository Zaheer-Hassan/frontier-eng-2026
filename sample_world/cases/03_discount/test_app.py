import pytest

from app import apply_discount


def test_ten_percent():
    assert apply_discount(100.0, 10.0) == 90.0


def test_zero_percent():
    assert apply_discount(80.0, 0.0) == 80.0


def test_full_discount():
    assert apply_discount(50.0, 100.0) == 0.0


def test_rejects_bad_percent():
    with pytest.raises(ValueError):
        apply_discount(10.0, 150.0)
