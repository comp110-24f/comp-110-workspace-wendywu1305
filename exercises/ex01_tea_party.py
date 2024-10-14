"""My second exercise in COMP110."""

__author__: str = "730818500"


def main_planner(guests: int) -> None:
    """calculating the logistics of a tea party"""
    # main orchestrate the execution of a program and produce output
    print("A Cozy Tea Party for " + str(guests) + " People!")
    # concatenated string as intro
    print("Tea Bags: " + str(tea_bags(people=guests)))
    # call tea_bags, return num of tea bags as string
    print("Treats: " + str(treats(people=guests)))
    # call treats, return num of treats as string
    print("Cost: $" + str(cost(tea_count=tea_bags(guests), treat_count=treats(guests))))
    # pre-course.care: I spent a long time stuck on the last line
    # how to refer to tea_count=RV of tea_bags and treat_count=RV of treats?
    # directly call functions tea_count and treat_count in this print func
    # this turns into a new frame in the stack if you think as a memory diagram
    # can neglect "people=guests" in here to be moree concise
    # we know that "guests" is the argument, is the parameter "people"


def tea_bags(people: int) -> int:
    """compute the number of tea bags needed based on number of guests"""
    # every person gets 2 tea bags
    return people * 2


def treats(people: int) -> int:
    """compute the number of treats needed based on the number of teas"""
    # every person gets 1.5 times the amount of treats in respect to tea bags
    return int(tea_bags(people=people) * 1.5)  # call tea_bags with input num of people


def cost(tea_count: int, treat_count: int) -> float:
    """compute the cost of the tea bags and the treats combined"""
    # tea_count is the number of tea bags
    # treat_count is the number of treats
    return float(tea_count * 0.5 + treat_count * 0.75)
    # add both variables together with the respective costs


if __name__ == "__main__":
    """conditional statement to make program runnable"""
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
# these are at the end of my program b/c python reads from top to bottom,
# python does not know what the call "main_planner(guests)" means if at the top
