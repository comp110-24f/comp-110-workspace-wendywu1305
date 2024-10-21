__author__: str = "730818500"


def find_and_remove_max(input: list[int]) -> int:
    """find and return largest num, also remove all instances of large num"""
    # return -1 if empty list
    if input == []:
        return -1
    # find the largest num
    idx: int = 1
    num = input[0]
    while idx < len(input):
        if num < input[idx]:
            num = input[idx]
        idx += 1
    # remove all instances of large num
    ix: int = 0
    while ix < len(input):
        if num == input[ix]:
            input.pop(ix)
            ix += 0  # don't increase index if popped out the index
        else:
            ix += 1  # increase if no popping
    return num
