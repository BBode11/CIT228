import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.brandon = Employee("brandon", "bode", 70000)

    def test_give_default_raise(self):
        self.brandon.give_raise()
        self.assertEqual(self.brandon.annual_salary, 75000)

    def test_give_custom_raise(self):
        self.brandon.give_raise(7000)
        self.assertEqual(self.brandon.annual_salary, 77000)

if __name__ == '__main__':
    unittest.main()
