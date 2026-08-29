"""Sum all integers from low to high, inclusive."""


def sum_inclusive(low: int, high: int) -> int:
    if low > high:
        low, high = high, low
    # BUG: off-by-one — excludes `high`
    total = 0
    n = low
    while n < high:
        total += n
        n += 1
    return total
