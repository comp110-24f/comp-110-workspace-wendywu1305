"""examples of dictionary syntax with Ice Cream Shop order tallies."""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

# len evaluates to the num of entries
print(len(ice_cream))  # prints 3

# add key-value entry by directly assigning to a key
ice_cream["mint"] = 3  # add mint as a new flavor, and 3 ppl want it

# access entries by their key
print(ice_cream["chocolate"])  # prints 12

# test if "pbj" is a key in ice_cream
has_pbj: bool = "pbj" in ice_cream  # will evaluate into True/False
# should have in globals has_pbj assigned to False

# to remove entry, use pop
ice_cream.pop("strawberry")

# to iterate overy every key in a loop, use for...in loop
for flavor in ice_cream:
    tally: int = ice_cream[flavor]  # count of ppl as value
    print(f"{flavor} has {tally} orders")
