from app import dedupe_preserve_order


def test_preserves_first_seen_order():
    assert dedupe_preserve_order(["b", "a", "b", "c", "a"]) == ["b", "a", "c"]


def test_empty():
    assert dedupe_preserve_order([]) == []


def test_all_unique():
    assert dedupe_preserve_order([1, 2, 3]) == [1, 2, 3]


def test_all_same():
    assert dedupe_preserve_order(["x", "x", "x"]) == ["x"]
