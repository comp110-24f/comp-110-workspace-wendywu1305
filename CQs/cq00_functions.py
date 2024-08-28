"""My first challenge question in COMP110."""

__author__ = "730818500"


# Function Definition
def mimic(message: str) -> str:
    """repeats the message I input."""
    return message


# function call when interact on trailhead
# print(mimic(message=str))


# Main Function
def main() -> None:
    """the main function that pulls together my functions."""
    print(mimic(message=input("What is your message?")))


# Nested Function Call
if __name__ == "__main__":
    main()
