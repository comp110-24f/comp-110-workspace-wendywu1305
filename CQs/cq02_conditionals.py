"""CQ02 for September 13 Friday."""

__author__ = "730818500"


def guess_a_number() -> None:
    secret: int = 7
    # set local variable guess as int 7
    x = int(input("Guess a number: "))
    # ask the user to guess num as input and save as local variable
    print("Your guess was " + str(x))
    if x == secret:
        print("You got it!")
    elif x <= secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
