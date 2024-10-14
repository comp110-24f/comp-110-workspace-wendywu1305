"""CQ04 for September 27 Friday, (tornado day) practice importing and scope."""

__author__: str = "730818500"


def get_coords(xs: str, ys: str) -> None:
    ix: int = 0  # index for xs
    iy: int = 0  # index for ys
    while ix < len(xs):  # check the index of xs
        while iy < len(ys):  # check the index of ys
            print("(" + xs[ix] + "," + ys[iy] + ")")
            iy += 1  # loop within iy
        ix += 1
        iy = 0  # set iy back to 0 to restart the 2nd while loop
