"""reproducing tried and true abstraction"""

__author__: str = "730818500"


def all(input: list[int], check: int) -> bool:
    """indicating if all ints in list are the same as the given int."""
    idx = 0  # index that runs through the list
    default_bool = False
    correct_times = 0  # record correct times
    while idx < len(input):
        if check == input[idx]:
            correct_times += 1
        idx += 1
    if correct_times == len(input):  # change the bool if all elem are matching
        default_bool = True
    return default_bool


def max(input: list[int]) -> int:
    """return the largest int in the list."""
    idx: int = 1
    large_num: int = input[0]  # the num that records the largest
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")  # show error is empty list
    while idx < len(input):
        if input[idx] > large_num:
            large_num = input[idx]  # update large_num is the new comparison is bigger
        idx += 1
    return large_num


def is_equal(a: list[int], b: list[int]) -> bool:
    """check deep equality for 2 separate lists."""
    idx: int = 0
    true_false: bool = False  # default bool as False
    match_times: int = 0  # collect matching times
    while idx < len(a) and idx < len(b):
        if a[idx] == b[idx]:
            match_times += 1
        idx += 1
    if match_times == len(a) or match_times == len(b):
        true_false = True
    return true_false


def extend(c: list[int], d: list[int]) -> None:
    """mutate 1st list by appending  2nd list values to the end of it."""
    idx: int = 0  # circulates through d
    while idx < len(d):
        c.append(d[idx])  # add each elem of d onto c
        idx += 1
