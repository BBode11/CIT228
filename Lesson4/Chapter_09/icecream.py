from restaurant import Restaurant
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        print("\tHere are the flavors: ")
        for flavor in self.flavors:
            print("\t\t", flavor.title())