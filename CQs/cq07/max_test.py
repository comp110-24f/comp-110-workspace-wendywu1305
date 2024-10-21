"""test if max works."""

__author__: str = "730818500"

from CQs.cq07.find_max import find_and_remove_max


def test_max_return_value() -> None:
    """make sure returns the expect value (big num)"""
    a: list[int] = [9, 23, 5, 7, 19, 23]
    assert find_and_remove_max(a) == 23


def test_max_mutate() -> None:
    """make sure mutates in the expected way (take out big num)"""
    a: list[int] = [9, 23, 5, 7, 19, 23]
    find_and_remove_max(a)  # remember to go through the func first
    assert a == [9, 5, 7, 19]  # then assert new list


# edge case empty
def test_max_empty() -> None:
    """make sure return -1 for empty input list"""
    a: list[int] = []
    assert find_and_remove_max(a) == -1


# edge case 2 big nums together
def test_max_together() -> None:
    """make sure pop out both big nums"""
    a: list[int] = [9, 23, 23, 5, 7, 19]
    find_and_remove_max(a)  # it might only pop the 1st 23 and miss the 2nd
    assert a == [9, 5, 7, 19]
