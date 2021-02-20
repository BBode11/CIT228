print("\t*---------- Exercise 10-6 ----------*\n")

#try:
#    num1 = input("Please enter any number: ")
#    num1 = int(num1)
#    num2 = input("Please enter another number: ")
#    num2 = int(num2)

#except ValueError:
#    print("Sorry the format you have entered is not correct.")
#else:
#    sum = num1 + num2
#    print(str(num1) + " + " + str(num2) + " is equal to " + str(sum) + ".")


print("\t*---------- Exercise 10-7 ----------*\n")

quit = ""
while quit != "q":
    try:
        num1 = input("Please enter any number: (Enter q to quit) ")
        if num1 == "q":
            break;
        num1 = int(num1)
        num2 = input("Please enter another number: (Enter q to quit) ")
        if num2 == "q":
            break;
        num2 = int(num2)

    except ValueError:
        print("Sorry the format you have entered is not correct.")
    else:
        sum = num1 + num2
        print(str(num1) + " + " + str(num2) + " is equal to " + str(sum) + ".")
        quit = input("Would you like to play again? (Enter q to quit) ")