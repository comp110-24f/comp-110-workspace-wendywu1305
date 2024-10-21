"""try implementing some list utility funcs."""

__author__: str = "730818500"


def only_evens(input: list[int]) -> list[int]:
    """make a new list that contains only even elems of orginal list"""
    new: list[int] = []
    for elem in input:
        if elem % 2 == 0:
            new.append(elem)
    return new


def sub(input: list[int], st_ix: int, end_ix: int) -> list[int]:
    """make a new list with specified start and end index -1"""
    new: list[int] = []
    # if the start index is negative
    if st_ix < 0:
        st_ix = 0  # start from the beginning of list
    # if the end index is greater than len of list
    if end_ix > len(input):
        end_ix = len(input)  # end with the end of list
    idx: int  # goes through the range
    if len(input) == 0:
        new = []  # if empty input list, nothing adds to new
    else:
        for idx in range(st_ix, end_ix):
            new.append(input[idx])
    return new


def add_at_index(input: list[int], add_elem: int, idx: int) -> None:
    """add the specific elem at the index onto the list, modify"""
    if idx > len(input) or idx < 0:
        raise IndexError("Index is out of bounds for the input list")
    if idx == len(input):  # if adding to the end of the list
        input.append(add_elem)
    # how to append the elem at the designated index?
    input.append(0)  # add 0 to the end as a placeholder
    count: int = len(input) - 1  # start at the last index
    while count > idx:  # while loop backward
        input[count] = input[count - 1]
        count -= 1
    input[idx] = add_elem  # modify the duplicate index to the new num
