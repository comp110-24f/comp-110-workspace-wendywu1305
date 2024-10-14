"""some scope examples."""


def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with all instances of char removed."""
    copy: str = ""  # Set up empty str to copy values over
    index: int = 0  # local variable
    print(word)  # no error b/c already read "word" in globals
    while index < len(msg):
        # if the letter is not char
        if msg[index] != char:  # or if not (msg[index] == char)
            copy += msg[index]  # add it to copy
        index += 1
    return copy


word: str = "yoyo"
print(remove_chars(word, "o"))

if __name__ == "__main__":
    # creat a variable called word with the value "yoyo"
    # this is outside the func def, so global variable
    # Print the result of calling your function with arguments word and “y”
    print(remove_chars(msg=word, char="y"))  # key word argument
# Print the result of calling your function with arguments word and “y”

# position argument, arguments connected to order in sig

# print(remove_chars(msg="footbal", char="o"))
