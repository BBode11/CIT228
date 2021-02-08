from random import randint
print("\n\t\t***---------- Exercise 9-13 Extra Credit ----------***")

class Dice():
    def __init__(self, sides=6):
        self.sides=sides
    def roll_die(self):
        return randint(1, self.sides)

#standard die rolled 10x
standardDie = Dice()
results = []
for num in range(10):
    result = standardDie.roll_die()
    #save to results
    results.append(result)
print(f"Standard Die Results = {results}")

print("\n\t\t***---------- Ten Sided Die ----------***")
#10 sided die rolled 10x

tenSided = Dice(sides=10)
results = []
for num in range(10):
    result = tenSided.roll_die()
    #save to results
    results.append(result)
print(f"Ten Sided Die Results = {results}")

print("\n\t\t***---------- Twenty Sided Die ----------***")
twentySided = Dice(sides=20)
results = []
for num in range(10):
    result = twentySided.roll_die()
    #save to results
    results.append(result)
print(f"Twenty Sided Die Results = {results}")