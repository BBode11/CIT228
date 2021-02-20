import unittest
from restaurant import Restaurant

class TestRestaurant(unittest.TestCase):
    def setUp(self):
        restaurant_name = "Bubbas"
        cuisine_type = "American"
        number_served = 10
        self.restaurant = Restaurant(restaurant_name, cuisine_type, number_served)
    def test_number_served_int(self):
        number_served = 15
        self.restaurant.set_number_served(number_served)
        self.assertEqual(self.restaurant.number_served, 15)

    def test_number_served_string(self):
        number_served = "15"
        self.restaurant.set_number_served(number_served)
        self.assertEqual(self.restaurant.number_served, 15)

    def test_increment_number_served_int(self):
        restaurant = 25
        self.restaurant.increment_number_served(restaurant)
        self.assertEqual(self.restaurant.number_served, 35)


    def test_increment_number_served_string(self):
        restaurant = "25"
        self.restaurant.increment_number_served(restaurant)
        self.assertEqual(self.restaurant.number_served, 35)

if __name__ == "__main__":
    unittest.main()