"""Simple FIFO queue."""


class Queue:
    def __init__(self) -> None:
        self._items: list = []

    def push(self, value) -> None:
        self._items.append(value)

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty queue")
        # BUG: LIFO — pops from the end instead of the front
        return self._items.pop()

    def __len__(self) -> int:
        return len(self._items)
