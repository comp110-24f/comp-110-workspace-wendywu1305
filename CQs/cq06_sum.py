"""Summing the elements of a list using different loops."""

# CQ06 for October 9 Wednesday

__author__: str = "730818500"


def w_sum(vals: list[float]) -> float:
    """add up all elements w/ while loop."""
    index: int = 0
    total_sum: float = 0.0
    while index < len(vals):
        total_sum += vals[index]
        index += 1
    return total_sum


def f_sum(vals: list[float]) -> float:
    """add up all elements w/ for loop."""
    total_sum: float = 0.0
    for elem in vals:
        total_sum += elem
    return total_sum


def f_range_sum(vals: list[float]) -> float:
    """add up all elements with for...in range() loop."""
    total_sum: float = 0.0
    for idx in range(0, len(vals)):
        total_sum += vals[idx]
    return total_sum
