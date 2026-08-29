from app import reverse_words


def test_basic():
    assert reverse_words("hello world") == "world hello"


def test_three_words():
    assert reverse_words("one two three") == "three two one"


def test_single_word():
    assert reverse_words("solo") == "solo"


def test_extra_internal_space_normalized_by_split_join_contract():
    # Implementation should split on spaces and re-join with single spaces
    assert reverse_words("a  b") == "b a"
