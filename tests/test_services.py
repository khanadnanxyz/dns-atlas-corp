import unittest

from web.services import calc_location


class Testing(unittest.TestCase):
    def test_calculation_success(self):
        id = 1
        x = 123.12
        y = 456.56
        z = 789.89
        vel = 20.0
        result = calc_location(id, x, y, z, vel)
        self.assertEqual(result, 1389.57)

    def test_string_float(self):
        id = 1
        x = "123.12"
        y = "456.56"
        z = "789.89"
        vel = "20.0"
        result = calc_location(id, x, y, z, vel)
        self.assertEqual(result, 1389.57)

