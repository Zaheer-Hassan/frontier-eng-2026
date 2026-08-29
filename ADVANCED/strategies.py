"""Repair strategies for the advanced bug-fix agent.

Each strategy is a named, reversible-style transformation. The agent selects
among unused strategies using failure text + source features (lightweight plan).
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Strategy:
    name: str
    apply: Callable[[str], str | None]


def _sub_once(pattern: str, repl: str, source: str, flags: int = 0) -> str | None:
    new, n = re.subn(pattern, repl, source, count=1, flags=flags)
    return new if n else None


def strategy_while_lt_to_le(source: str) -> str | None:
    return _sub_once(r"while\s+(\w+)\s*<\s*(\w+)\s*:", r"while \1 <= \2:", source)


def strategy_sorted_drop_reverse(source: str) -> str | None:
    return _sub_once(
        r"sorted\((.+?),\s*reverse\s*=\s*True\)",
        r"sorted(\1)",
        source,
    )


def strategy_queue_pop0(source: str) -> str | None:
    return _sub_once(r"self\._items\.pop\(\)", "self._items.pop(0)", source)


def strategy_reverse_words(source: str) -> str | None:
    if "def reverse_words" not in source:
        return None
    if "sentence[::-1]" not in source and "[::-1]" not in source:
        # Already looks non-naive; skip unless still failing later via other means
        if "reversed(" in source and "split" in source:
            return None
    replacement = (
        'def reverse_words(sentence: str) -> str:\n'
        '    parts = [p for p in sentence.split(" ") if p != ""]\n'
        '    return " ".join(reversed(parts))\n'
    )
    new = re.sub(
        r"def reverse_words\(sentence: str\) -> str:.*?$",
        replacement.rstrip(),
        source,
        count=1,
        flags=re.S,
    )
    return new if new != source else None


def strategy_discount_percent(source: str) -> str | None:
    if "price - percent" not in source and "price-percent" not in source:
        return None
    new = _sub_once(
        r"return\s+price\s*-\s*percent",
        "return price * (1.0 - (percent / 100.0))",
        source,
    )
    return new


def strategy_dedupe_dict_order(source: str) -> str | None:
    if "set(items)" not in source:
        return None
    new = _sub_once(
        r"return\s+sorted\(set\(items\)\)",
        "return list(dict.fromkeys(items))",
        source,
    )
    if new:
        return new
    return _sub_once(
        r"return\s+list\(set\(items\)\)",
        "return list(dict.fromkeys(items))",
        source,
    )


def strategy_slugify_lower(source: str) -> str | None:
    if "def slugify" not in source:
        return None
    # Rewrite function body to correct policy.
    replacement = (
        "def slugify(title: str) -> str:\n"
        "    import re\n"
        "    cleaned = re.sub(r\"[^a-zA-Z0-9]+\", \"-\", title.strip().lower())\n"
        "    cleaned = re.sub(r\"-+\", \"-\", cleaned)\n"
        "    return cleaned.strip(\"-\")\n"
    )
    new = re.sub(
        r"def slugify\(title: str\) -> str:.*?$",
        replacement.rstrip(),
        source,
        count=1,
        flags=re.S,
    )
    return new if new != source else None


def strategy_password_policy(source: str) -> str | None:
    if "is_valid_password" not in source:
        return None
    replacement = (
        "def is_valid_password(password: str) -> bool:\n"
        "    if len(password) < 8:\n"
        "        return False\n"
        "    if any(ch.isspace() for ch in password):\n"
        "        return False\n"
        "    has_upper = any(ch.isupper() for ch in password)\n"
        "    has_lower = any(ch.islower() for ch in password)\n"
        "    has_digit = any(ch.isdigit() for ch in password)\n"
        "    symbols = set(\"!@#$%^&*\")\n"
        "    has_symbol = any(ch in symbols for ch in password)\n"
        "    return has_upper and has_lower and has_digit and has_symbol\n"
    )
    new = re.sub(
        r"def is_valid_password\(password: str\) -> bool:.*?$",
        replacement.rstrip(),
        source,
        count=1,
        flags=re.S,
    )
    return new if new != source else None


STRATEGIES: list[Strategy] = [
    Strategy("while_lt_to_le", strategy_while_lt_to_le),
    Strategy("sorted_drop_reverse", strategy_sorted_drop_reverse),
    Strategy("queue_pop0", strategy_queue_pop0),
    Strategy("reverse_words", strategy_reverse_words),
    Strategy("discount_percent", strategy_discount_percent),
    Strategy("dedupe_dict_order", strategy_dedupe_dict_order),
    Strategy("slugify_lower", strategy_slugify_lower),
    Strategy("password_policy", strategy_password_policy),
]


def plan_next_strategy(
    source: str,
    pytest_output: str,
    tried: set[str],
) -> Strategy | None:
    """Lightweight planner: rank unused strategies by signal overlap."""

    text = (source + "\n" + pytest_output).lower()
    scores: list[tuple[int, Strategy]] = []
    for strat in STRATEGIES:
        if strat.name in tried:
            continue
        score = 0
        if strat.name == "while_lt_to_le" and ("while" in text and "<" in source):
            score += 3
        if strat.name == "sorted_drop_reverse" and "reverse" in text:
            score += 4
        if strat.name == "queue_pop0" and ("queue" in text or "pop" in text):
            score += 3
        if strat.name == "reverse_words" and ("[::-1]" in source or "reverse_words" in text):
            score += 5
        if strat.name == "discount_percent" and ("discount" in text or "percent" in text):
            score += 4
        if strat.name == "dedupe_dict_order" and ("set(" in source or "dedupe" in text):
            score += 4
        if strat.name == "slugify_lower" and "slugify" in text:
            score += 5
        if strat.name == "password_policy" and ("password" in text or "symbol" in text):
            score += 5
        # Prefer strategies that can actually transform current source.
        if strat.apply(source) is None:
            score -= 10
        scores.append((score, strat))

    scores.sort(key=lambda x: x[0], reverse=True)
    if not scores or scores[0][0] <= 0:
        # Fallback: first unused strategy that changes source
        for strat in STRATEGIES:
            if strat.name in tried:
                continue
            if strat.apply(source) is not None:
                return strat
        return None
    return scores[0][1]
