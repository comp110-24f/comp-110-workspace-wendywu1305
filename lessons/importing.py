"""practice importing."""

from lessons.scope_practice import remove_chars

# without the next line, we are only importing the func def
# but we dont have a function call yet
# so the output would be whatever output from original

# you can import multiple things from the orginal module
# eg. you can do both the func and the global variable

print(remove_chars("happy", "p"))
