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