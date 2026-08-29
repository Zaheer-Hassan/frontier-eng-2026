from app import is_valid_password


def test_valid_example():
    assert is_valid_password("Abcd123!") is True


def test_missing_symbol():
    assert is_valid_password("Abcd1234") is False


def test_underscore_is_not_enough():
    # underscore is not in the allowed symbol set
    assert is_valid_password("Abcd123_") is False


def test_too_short():
    assert is_valid_password("Ab1!") is False


def test_rejects_whitespace():
    assert is_valid_password("Abcd 123!") is False


def test_needs_upper_lower_digit_symbol():
    assert is_valid_password("abcdefgh1!") is False
    assert is_valid_password("ABCDEFGH1!") is False
    assert is_valid_password("Abcdefgh!") is False
