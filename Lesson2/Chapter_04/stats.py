import random

number = random.randrange(10,100)
numberList = list(range(number))
print(numberList)

print("The largest number is: ", max(numberList))
print("The smallest number is: ", min(numberList))
print("The total of all the numbers is: ", sum(numberList))
print("The average number is: ", sum(numberList)/len(numberList))