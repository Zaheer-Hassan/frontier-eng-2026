from app import slugify


def test_basic():
    assert slugify("Hello World") == "hello-world"


def test_punctuation():
    assert slugify("Hello, World!") == "hello-world"


def test_trims_edges():
    assert slugify("  Already--Slug  ") == "already-slug"


def test_numbers_ok():
    assert slugify("Top 10 Tips") == "top-10-tips"
