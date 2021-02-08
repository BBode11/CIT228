print("***---------- Exercise 9-1 ----------***")
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")
              
restaurant=Restaurant("Buffalo Wild Wings", "American")
print("The restaurant name is ", restaurant.restaurant_name)
print("The restaurant cuisine is ", restaurant.cuisine_type)
restaurant.open_restaurant()
restaurant.describe_restaurant()



print("***---------- Exercise 9-2 ----------***")
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

bdubs=Restaurant("Buffalo Wild Wings", "American")
bdubs.describe_restaurant()
tBell=Restaurant("Taco Bell", "Mexican")
tBell.describe_restaurant()
aBuffet=Restaurant("Asian Buffet", "Chinese")
aBuffet.describe_restaurant()

print("***---------- Exercise 9-4 ----------***")
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=number_served

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

    def set_number_served(self, served):
        self.number_served=int(served)

    def increment_number_served(self, served):
        self.number_served += int(served)


bdubs=Restaurant("Buffalo Wild Wings", "American", 6)
bdubs.describe_restaurant()
print("The number of customers initially served is ", bdubs.number_served)
bdubs.number_served = 20
print("The new number of customers served is ", bdubs.number_served)

served = input("How many customers have been served?")
bdubs.set_number_served(served)
print("The number of customers served is ", bdubs.number_served)

served = input("How many additional customers have been served?")
bdubs.increment_number_served(served)
print("The total number of customers served is ", bdubs.number_served)
