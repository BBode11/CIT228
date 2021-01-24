print("*---------- Exercise 5-1 ----------*")

color = "Blue"
number1 = 15
number2 = 20
number3 = 50
carBrands = ["Chevy", "Ford", "GMC", "Chrysler", "Dodge", "Tesla", "Subaru"]

print("***--------------- True Results ---------------***")
print(number1, "<", number2, number1<number2)
print(number1, "<=", number2, number1<=number2)
print(number3, ">", number1, number3>number1)
print("Chevy is a car brand.", carBrands[0] == 'Chevy')
print(number3, ">=", number2, number3>=number2)

print("***--------------- False Results ---------------***")
print(number2, "<", number1, number2<number1)
print(number2, "<=", number1, number2<=number1)
print(number1, ">", number3, number1>number3)
print("Toad is a car brand.", carBrands[0:7] == "Toad")
print(number2, ">=", number3, number2>=number3)

print("*---------- Exercise 5-2 ----------*")
print(color, "==", "Blue", color == "Blue")
print(color, "!=", "Blue", color == "Blue")
print("blue == blue", color.lower()=="blue")

print(number2, "<=", number3, "and", number2, ">", number1, number2<=number3 and number2 > number1)

