"""CQ03 for September 18 Wednesday, practice while loops."""

__author__: str = "730818500"


def num_instances(phrase: str, search_char: str) -> None:
    """function that counts times char in phrase = searched char"""
    count: int = 0  # counts the number of occurence of char in phrase
    index: int = 0  # indicates the index we're looking at on phrase
    while index < len(phrase):  # active when index less than phrase char num
        if search_char == phrase[index]:
            count += 1  # if same, count + 1
        else:
            count += 0  # if not, don't count
        index += 1  # add index for next cycle in loop
    print(count)
    # I initially made the mistake of not print but returning
    # then I accidentally asked to prin "index" instead of "count"
