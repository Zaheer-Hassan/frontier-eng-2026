"""Validate passwords against a small policy.

Policy:
- length >= 8
- at least one uppercase letter
- at least one lowercase letter
- at least one digit
- at least one symbol from !@#$%^&*
- must not contain whitespace
"""


def is_valid_password(password: str) -> bool:
    if len(password) < 8:
        return False
    if any(ch.isspace() for ch in password):
        return False
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    # BUG (hard): symbol check is wrong — treats underscore as required symbol set only,
    # and ignores !@#$%^&* ; also returns True if upper+lower+digit even without symbol
    has_symbol = "_" in password
    return has_upper and has_lower and has_digit
