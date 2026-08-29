"""Apply a percent discount to a price. percent is 0..100."""


def apply_discount(price: float, percent: float) -> float:
    if price < 0:
        raise ValueError("price must be non-negative")
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    # BUG: treats percent as a fraction already (50 -> subtract 50) for mid values,
    # and mishandles by doing price - percent instead of price * (1 - percent/100)
    return price - percent
