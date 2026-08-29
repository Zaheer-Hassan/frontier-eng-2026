"""Reverse the order of words in a sentence; preserve single spaces between words."""


def reverse_words(sentence: str) -> str:
    parts = sentence.split(" ")
    # BUG: reverses characters of the whole string instead of word order
    return sentence[::-1]
