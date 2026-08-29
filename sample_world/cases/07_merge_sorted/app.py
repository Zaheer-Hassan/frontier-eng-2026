"""Merge two ascending sorted lists into one ascending sorted list."""


def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    # BUG: concatenates then sorts descending
    return sorted(a + b, reverse=True)
