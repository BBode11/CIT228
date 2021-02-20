print("\t*---------- Exercise 10-3 ----------*")
filename = "Chapter_10/guests.txt"

'''name = input("What is your name? (q to quit)")
with open(filename, "w") as textFile:
    while name != "q":
        name += "\n"
        textFile.write(name)
        name = input("What is your name? (q to quit)")'''

print("\t*---------- Exercise 10-4 ----------*")
filename = "Chapter_10/guest_book.txt"

import random
import os
#delete text file if existing
if os.path.exists(filename):
    os.remove(filename)
# creating a new file
seats=[]
with open(filename, "w") as guestBook:
    guest = input("What is your name? (Type q to quit) ")
    while guest != "q":
        print(f"Thanks for registering {guest}, we will be with you as soon as possible.")
        number = random.randint(1, 10)
        while number in seats:
            number = random.randint(1, 10)
        print(f"{guest} you are going to be seated at table number {number}.")
        seats.append(number)
        guest +=", table # " + str(number) + "\n"
        guestBook.write(guest)
        guest = input("What is your name? (Type q to quit) ")
#reading from new text file
with open(filename) as guestBook:
    print("---------------Guest Book--------------\n")
    for line in guestBook:
        print(line)