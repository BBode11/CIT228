print("*---------- 8-12 ----------*\n")
def cust_sandwich(*extras):
    print("I make the best sandwiches on this side of the Mississippi!")
    for extra in extras:
        print(f"I'll add {extra} to your delicious sandwich!")
    print("Hope you enjoy the best sandwich on this side of the Mississippi!")

cust_sandwich("Honey Ham", "Swiss Cheese", "Mayo", "Lettuce")
print("")
cust_sandwich("Bacon", "Lettuce", "Tomato", "Mayo")
print("")
cust_sandwich("Grilled Chicken", "Cheddar Cheese", "Lettuce", "Tomato", "Mayo")
