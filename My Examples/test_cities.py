import unittest

from city_functions import get_city_country

class CitiesTestcase(unittest.TestCase):
    """ Test for city_functions """

    def test_get_city_country(self):
        """ Does the cities look like Paris, France? """
        formatted_city = get_city_country("paris","france")
        self.assertEqual(formatted_city,'Paris, France')

unittest.main()