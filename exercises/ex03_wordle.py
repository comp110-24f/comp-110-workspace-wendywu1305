"""My fourth exercise, Wordle, a fun exploratin of emojis and f-strings."""

__author__: str = "730818500"

# input_word is the name for the guessed word
# secret_word is the name for the actual word
WHITE_BOX: str = "\U00002B1C"  # global variables of the emoji strings
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def input_guess(secret_word_len: int) -> str:
    """prompt the user to enter a guess and continue prompting until correct length."""
    input_word: str = input(f"Enter a {secret_word_len} character word: ")
    while len(input_word) != secret_word_len:
        # if len isn't correct, reassign by asking for input
        input_word = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return input_word  # if len correct, return input word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """check if each index of secret_word matches the char, 1 match is good for True."""
    assert len(char_guess) == 1
    ix: int = 0  # index that goes though the word to look for match
    while ix < len(secret_word):
        if secret_word[ix] == char_guess:
            ix = len(char_guess)  # end the while loop
            return True
        else:
            ix += 1
    return False


def emojified(input_word: str, secret_word: str) -> str:
    """compare the user's guess and the secret word, return a string of emojis."""
    assert len(input_word) == len(secret_word)
    ix: int = 0  # track index
    result_string: str = ""  # give an empty string to concatenate emojis
    while ix < len(secret_word):
        if input_word[ix] == secret_word[ix]:
            result_string += GREEN_BOX
            # total match, green box
        elif contains_char(secret_word, input_word[ix]) is True:
            result_string += YELLOW_BOX
            # wrong place but letter exist, yellow box
        else:
            result_string += WHITE_BOX
            # completely wrong letter, white box
        ix += 1
    return result_string  # return the complete string of emojis


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1  # records how many times the user attempts
    total_turns: int = 6
    win_lose: bool = False  # default to keep the while loop going
    while turns <= total_turns and win_lose is False:
        print(f"=== Turn {turns}/{total_turns}  ===")  # print out during each trial
        input_word = input_guess(len(secret))
        # call input_guess func to ask for input, assign user's guess as "input_word"
        print(emojified(input_word, secret))
        # call emojified to print out the string of emojis
        if input_word == secret:
            win_lose = True  # change condition to stop loop
            print(f"You won in {turns}/6 turns!")
        turns += 1
    # still cannot guess after all 6 trials
    if win_lose is False:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
