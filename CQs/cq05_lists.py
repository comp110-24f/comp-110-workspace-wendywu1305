"""CQ05 for October 4 Friday, mutating functions."""

__author__: str = "730818500"

list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


def manual_append(a_list: list[int], an_int: int) -> None:
    a_list.append(an_int)


def double(a_list: list[int]) -> None:
    ix: int = 0
    while ix < len(a_list):
        a_list[ix] = a_list[ix] * 2
        ix += 1


double(list_2)
print(list_1)
print(list_2)
