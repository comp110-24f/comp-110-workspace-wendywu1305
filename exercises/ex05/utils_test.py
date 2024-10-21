"""define unit tests for util."""

__author__: str = "730818500"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens() -> None:
    """make sure retun new list with only even nums."""
    a: list[int] = [2, 5, 3, 6, 10, 25]
    assert only_evens(a) == [2, 6, 10]


def test_sub() -> None:
    """make sure return new list with specified elems from idx."""
    b: list[int] = [2, 3, 5, 7, 11, 13]
    assert sub(b, 2, 5) == [5, 7, 11]


# edge case of sub
def test_sub_empty() -> None:
    """make sure sub empty input return empty list."""
    c: list[int] = []
    assert sub(c, 1, 3) == []


# edge case of sub
def test_sub_out_range() -> None:
    """make sure big index gets fixed."""
    b: list[int] = [2, 3, 5, 7, 11, 13]
    assert sub(b, 2, 10) == [5, 7, 11, 13]


def test_add_at_index() -> None:
    """test if adding elem not at the end of a list."""
    c: list[int] = [2, 4, 6, 8]
    add_at_index(c, 5, 2)
    assert c == [2, 4, 5, 6, 8]


# test index error for add_at_index
def test_add_at_index_raise_error() -> None:
    """make sure raise an IndexError for an invalid index."""
    c: list[int] = [2, 4, 6, 8]
    with pytest.raises(IndexError):
        add_at_index(c, 10, 10)
