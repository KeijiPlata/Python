# Activity 11-1 City, Country (test)

# to create a test case we need to import unittest
import unittest

# import the package we need to test
from city_functions import cityCountry as cc

# to create test cases, we need to put in a class that inherits unittest
class CityCountryTest(unittest.TestCase):
    """Test for city_functions.py"""

    # all the methods should start with "test_" so the program will recognize
    # what to test
    # self.assertEqual() accepts two parameters and compare both of them
    def test_city_country(self):
        """Test if the string is concatenated and if there is a comma in middle"""
        formatted_cityCountryName = cc('Manila', 'Philippines')
        self.assertEqual(formatted_cityCountryName, 'Manila, Philippines')

    def test_small_letters(self):
        """Test if the functions can accept small letters and convert to title()"""
        formatted_cityCountryName = cc('santiago', 'chile')
        self.assertEqual(formatted_cityCountryName, 'Santiago, Chile')

    def test_city_country_population(self):
        """Test if the function can accept population"""
        formatted_cityCountryName = cc('santiago', 'chile', 5000000)
        self.assertEqual(formatted_cityCountryName, 'Santiago, Chile - Population 5000000')

# runs the test cases
if __name__ == '__main__':
    unittest.main()