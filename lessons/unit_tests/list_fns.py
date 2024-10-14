def get_first(a: list[str]) -> str:
    """Takes a list[str] as input and returns first elem."""
    if len(a) == 0:  # if empty list
        return ""  # return empty list
    return a[0]  # else return first


def remove_first(b: list[str]) -> None:
    """Take a list[str] as input and remove 1st elem."""
    b.pop(0)


def get_and_remove_first(c: list[str]) -> str:
    """returns AND remove first elem."""
    first_elem: str = c[0]  # store the first elem before removing
    c.pop(0)
    return first_elem
