"""Convert a title into a URL slug: lowercase, hyphen-separated, alphanumerics only."""

import re


def slugify(title: str) -> str:
    # BUG: does not lowercase; also collapses poorly and keeps underscores
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "-", title.strip())
    return cleaned.strip("-")
