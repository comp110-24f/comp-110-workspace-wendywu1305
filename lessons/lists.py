"""basic syntax of lists."""

# create an empty list
my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

# String Analogy
# my_name : str = "" # literal
# my_name : str = str() # constructor

# adding a value to a list
my_numbers.append(1.5)  # added the number 1.5
my_numbers.append(2.3)
# print(my_numbers)

# creating an already populated list
game_points: list[int] = [102, 86, 94]
print(game_points)

# suscription notation/indexing
print(game_points[2])  # will print out the 3rd number 94
last_game: int = game_points[2]
print(last_game)

# modifying by index (lists are mutable)
game_points[1] = 72  # changes 86 to 72

# getting the length
print(len(game_points))

# remove an item from list
game_points.pop(1)  # remove 72, type its index in ()


def display(int_list: list[int]) -> None:
    """displays all int"""
    index: int = 0
    while index < len(int_list):
        print(int_list[index])
        index += 1


display(int_list=game_points)


grocery_list: list[str] = ["banana", "banana", "happy"]
grocery_list.append("happy")
