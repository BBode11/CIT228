print("***---------- Exercise 9-6 ----------***")
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        #self.number_served=number_served

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

    #def set_number_served(self, served):
    #    self.number_served=int(served)

    #def increment_number_served(self, served):
    #    self.number_served += int(served)


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        print("\tHere are the flavors: ")
        for flavor in self.flavors:
            print("\t\t", flavor.title())

frosty_cup = IceCreamStand("The Frosty Cup")
frosty_cup.flavors = ["Bacon", "Maple", "Chocolate", "Vanilla", "Cherry Pecan", "Heath"]

frosty_cup.describe_restaurant()
frosty_cup.display_flavors()