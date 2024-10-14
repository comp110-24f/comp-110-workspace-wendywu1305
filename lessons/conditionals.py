"""Practice with conditionals."""


def less_than_10(num: int) -> None:
    """tell me if num is < 10"""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("Small number!")
    else:
        print("Big number!")
    print("Have a nice day!")


(less_than_10(num=5))


def should_I_eat(hungry: bool) -> None:
    """tells me wheter or not to eat based on hunger"""
    if hungry:  # conditional/boolean expression
        print("Eat some food silly goose!")  # "then" block
    else:
        print("Do your Comp 110 homework instead.")  # "else" block
    print("I'm proud of you <3")  # either way, be kind to yourself :)


should_I_eat(hungry=True)


def check_first_letter(word: str, letter: str) -> str:
    """check if letter is first character of word"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="h"))
