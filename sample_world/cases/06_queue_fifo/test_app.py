import pytest

from app import Queue


def test_fifo_order():
    q = Queue()
    q.push("a")
    q.push("b")
    q.push("c")
    assert q.pop() == "a"
    assert q.pop() == "b"
    assert q.pop() == "c"


def test_length():
    q = Queue()
    assert len(q) == 0
    q.push(1)
    assert len(q) == 1
    q.pop()
    assert len(q) == 0


def test_empty_pop():
    q = Queue()
    with pytest.raises(IndexError):
        q.pop()
