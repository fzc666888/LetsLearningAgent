import pytest

from textutil import count_words, strip_whitespace, truncate


def test_strip_whitespace_normal() -> None:
    assert strip_whitespace("  hello world  ") == "hello world"


def test_strip_whitespace_empty() -> None:
    assert strip_whitespace("") == ""
    assert strip_whitespace("   ") == ""


def test_truncate_normal() -> None:
    assert truncate("hello", 3) == "hel"


def test_truncate_length_boundary() -> None:
    assert truncate("hello", 5) == "hello"
    assert truncate("hello", 0) == ""


def test_truncate_empty() -> None:
    assert truncate("", 3) == ""


def test_truncate_rejects_negative_length() -> None:
    with pytest.raises(ValueError):
        truncate("hello", -1)


def test_count_words_normal() -> None:
    assert count_words("hello world") == 2
    assert count_words("  one   two  three ") == 3


def test_count_words_empty() -> None:
    assert count_words("") == 0
    assert count_words("   ") == 0
