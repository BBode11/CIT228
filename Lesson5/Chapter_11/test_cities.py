import unittest
from city_functions import get_formatted_city

class CitiesTestCase(unittest.TestCase):
   def test_get_formatted_city(self):
        cadillac_usa = get_formatted_city('cadillac', 'usa')
        self.assertEqual(cadillac_usa, 'Cadillac, Usa')

   def test_get_formatted_city_population(self):
        cadillac_usa = get_formatted_city('cadillac', 'usa', population = 10000)
        self.assertEqual(cadillac_usa, 'Cadillac, Usa - Population: 10000')

if __name__ == '__main__':
    unittest.main()
