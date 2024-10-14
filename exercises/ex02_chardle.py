"""My third exercise, Chardle, a pre-program for Wordle."""

__author__: str = "730818500"


def input_word() -> str:
    """func to for user to input word."""
    word: str = input("Enter a 5-character word: ")
    # ask user to guess a word and set as local var "word"
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")  # if not 5 char, print error
        exit()  # stop the program going further
        # no else block if nothing happens
    return word


def input_letter() -> str:
    """func to prompt user to enter 1 character."""
    letter: str = input("Enter a single character: ")
    # ask user to input a letter and save as local var "letter"
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()  # if not 1 character, print error and stop the program
        # no else block if nothing happens
    return letter


def contains_char(word: str, letter: str) -> None:
    """check if the input character matches any of the letters in input word"""
    # parameters from previous 2 functions
    print("Searching for " + letter + " in " + word)
    # all lines below checks if input letter matches input word on indices
    instance: int = 0  # number of times the input letter matches in input word
    if letter == word[0]:  # check 1st letter
        print(letter + " found at index 0")
        instance += 1
    if letter == word[1]:  # check 2nd letter
        print(letter + " found at index 1")
        instance += 1
    if letter == word[2]:  # check 3rd letter
        print(letter + " found at index 2")
        instance += 1
    if letter == word[3]:  # check 4th letter
        print(letter + " found at index 3")
        instance += 1
    if letter == word[4]:  # check 4th letter
        print(letter + " found at index 4")
        instance += 1
    if instance < 1:
        print("No instances of " + letter + " found in " + word)
    elif instance == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(instance) + " instances of " + letter + " found in " + word)
    # I don't know why it doesn't print out the "no instance" option
    # after tutoring: I did index instad of instances,
    # b/c by the end of the loop, index would be 5


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())
    # call input_word and input_letter here,
    # instead of in the contains_char signature


if __name__ == "__main__":
    """conditional statement to make program runnable"""
    main()
