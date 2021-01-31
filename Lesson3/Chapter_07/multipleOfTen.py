multiple = input("Please enter a number and I will tell you if it is a multiple of 10: ")
multiple = int(multiple)

if multiple %10 == 0:
    print("The number", multiple, "is a multiple of ten.")
else:
    print("The number", multiple, "is not a multiple of ten.")
