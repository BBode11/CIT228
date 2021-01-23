animals = ["Cow", "Chicken", "Duck", "Goat", "Horse", "Pig"]

print("---------- Original List ----------")
for item in animals:
    print(item)

print("---------- New List ----------")
yourAnimals = animals[:]
yourAnimals.append("Deer")
yourAnimals.append("Elk")
yourAnimals.append("Turkey")
yourAnimals.append("Bull")

for item in yourAnimals:
    print(item)

print("*-------------- Exercise 4-10 ---------------*")
print("The first three animals in the list are: ", yourAnimals[0:3])
print("Three animals from the middle of the list are: ", yourAnimals[4:7])
print("The last three animals in the list are: ", yourAnimals[7:10])