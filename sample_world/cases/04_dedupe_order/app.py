"""Deduplicate items while preserving first-seen order."""


def dedupe_preserve_order(items: list) -> list:
    # BUG: dedupes but sorts, destroying first-seen order
    return sorted(set(items))
