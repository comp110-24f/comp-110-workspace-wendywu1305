"""Practice with function."""

from random import randint

print(randint(3, 15))


# Function Definition
def sum(num1: int, num2: int) -> int:
    # parameters in (), the whole line is signature
    """return the sum of num1 and num2."""
    return num1 + num2


# Function Call
print(sum(num1=2, num2=13))  # <- arguments in ()
