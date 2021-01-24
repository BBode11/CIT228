print("*---------- Exercise 5-8 ----------*")
usernames = ["Brandon", "Bill", "Brian", "Emily", "Rachel", "Admin"]
for name in usernames:
    if name == "Admin":
        print("Hello", name.title(), "would you like to see a status report?")
    else:
        print("Hello", name.title(), "thank you for logging in again!")


print("\n*---------- Exercise 5-9 ----------*")
usernames = []
if usernames:
    for name in usernames:
        if name == "Admin":
             print("Hello", name.title(), "would you like to see a status report?")
        else:
            print("Hello", name.title(), "thank you for logging in again!")
else:
    print("We need to get some users!")

print("\n*---------- Exercise 5-10 ----------*")
current_users = ["brandon", "emily", "rachel", "paula", "branell"]
new_users = ["brandon", "emily", "haley", "max", "chloe"]
#***-------I used the setup for .lower from the online book portion---*

current_users_lower = [users.lower() for users in current_users]

for new in new_users:
    if new.lower() in current_users_lower:
        print(new.title(), "has been taken, please use something else.")
    else:
        print(new.title(), "is available.")






