print("---------- Exercise 3-4 ----------\n")
guestList = ["Branell", "Paula", "Kass"]
print(guestList[0], "will you be able to come over to dinner tonight?")
print(guestList[1], "you should come to dinner with", guestList[0], "tonight!")
print(guestList[2], "can you come over to dinner tonight?")


print("---------- Exercise 3-5 ----------\n")
print(guestList[1], "will not be able to attend dinner tonight.")
guestList[1] = "Emily"
print(guestList[0], "will you be able to come over to dinner tonight?")
print(guestList[1], "you should come to dinner with", guestList[0], "tonight!")
print(guestList[2], "can you come over to dinner tonight?")



print("---------- Exercise 3-6 ----------\n")
print(guestList[0], "I found a larger table so I will be inviting a few more people to dinner.")
print(guestList[1], "I found a larger table so I will be inviting a few more people to dinner.")
print(guestList[2], "I found a larger table so I will be inviting a few more people to dinner.")

guestList.insert(0, "Rachel")
guestList.insert(2, "Max")
guestList.append("Bryce")

print(guestList, "\n")
print(guestList[0], ", please join me and", len(guestList), "others for dinner tonight.")
print(guestList[1], ", please join me and", len(guestList), "others for dinner tonight.")
print(guestList[2], ", please join me and", len(guestList), "others for dinner tonight.")
print(guestList[3], ", please join me and", len(guestList), "others for dinner tonight.")
print(guestList[4], ", please join me and", len(guestList), "others for dinner tonight.")
print(guestList[5], ", please join me and", len(guestList), "others for dinner tonight.")


print("---------- Exercise 3-7 ----------\n")
print("It appears the table will not arrive before dinner.")
print("I will have to reduce the list and invite the others next week. \n")

print(guestList[5], "I am sorry but will you come to dinner next week? \n")
guestList.pop()

print(guestList[4], "I am sorry but will you come to dinner next week? \n")
guestList.pop()

print(guestList[3], "I am sorry but will you come to dinner next week? \n")
guestList.pop()

print(guestList[2], "I am sorry but will you come to dinner next week? \n")
guestList.pop()

print(guestList, "Can you two still attend dinner this week?")

del guestList[0]
del guestList[0]
print(guestList)
print("Guest list cleared for this week.")
