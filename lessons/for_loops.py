"""practice with for...in... loop."""

pets: list[str] = ["Louie", "Bo", "Bear"]
# tell each pet they are a good boy!
for pet_name in pets:  # call each element of the list "pet_name"
    print(f"Good boy, {pet_name}!")  # using f-string rather than concat


# range
for idx in range(0, len(pets)):
    print(pets[idx])  # use suscription notation


names: list[str] = ["Alyssa", "Janet", "Vrinda"]
# print every element's index and value
for idx in range(0, len(names)):
    print(f"{idx}: {names[idx]}")
