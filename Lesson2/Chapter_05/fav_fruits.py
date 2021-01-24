print("*---------- Exercise 5-7 ----------*")
favFruits = ["Oranges", "Strawberries", "Grapefruit", "Tomatoes"]
for fruit in favFruits:
    print("The fruit is: ", fruit)
    if fruit == "Oranges":
        print("Oranges are the color orange and they are delicious!")
    if fruit == "Strawberries":
        print("Strawberries are the color red and they are delicious!")
    if fruit == "Grapefruit":
        print("Grapefuit are the color pink and they are delicious!")
    if fruit != favFruits[0:3]:
        print("That is not my favorite fruit.")
    if fruit == "Tomatoes":
        print("I do not consider that a fruit")
