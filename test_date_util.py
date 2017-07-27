import unittest
from date_util import DateUtil


class TestDateUtil(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_is_leap_year_2016(self):
        self.assertTrue(DateUtil.is_leap_year(2016))

    def test_is_leap_year_2015(self):
        self.assertFalse(DateUtil.is_leap_year(2015))

    def test_is_leap_year_2000(self):
        self.assertTrue(DateUtil.is_leap_year(2000))

    def test_is_leap_year_2200(self):
        self.assertFalse(DateUtil.is_leap_year(2200))

    def test_day_of_year_0_1_1(self):
        self.assertRaises(AssertionError, DateUtil.day_of_year, 0, 1, 1)

    def test_day_of_year__1_1_1(self):
        self.assertRaises(AssertionError, DateUtil.day_of_year, -1, 1, 1)

    def test_day_of_year_2016_13_1(self):
        self.assertRaises(AssertionError, DateUtil.day_of_year, 2016, 13, 1)

    def test_day_of_year_2016_2_30(self):
        self.assertRaises(AssertionError, DateUtil.day_of_year, 2016, 2, 30)

    def test_day_of_year_2015_2_29(self):
        self.assertRaises(AssertionError, DateUtil.day_of_year, 2015, 2, 29)

    def test_day_of_year_2016_10_32(self):
        self.assertRaises(AssertionError, DateUtil.day_of_year, 2016, 10, 32)

    def test_day_of_year_1_1_1(self):
        self.assertEqual(DateUtil.day_of_year(1, 1, 1), 1)

    def test_day_of_year_2016_2_28(self):
        self.assertEqual(DateUtil.day_of_year(2016, 2, 28), 59)

    def test_day_of_year_2016_2_29(self):
        self.assertEqual(DateUtil.day_of_year(2016, 2, 29), 60)

    def test_day_of_year_2015_2_28(self):
        self.assertEqual(DateUtil.day_of_year(2015, 2, 28), 59)

    def test_day_of_year_2016_3_1(self):
        self.assertEqual(DateUtil.day_of_year(2016, 3, 1), 61)

    def test_day_of_year_2015_3_1(self):
        self.assertEqual(DateUtil.day_of_year(2015, 3, 1), 60)

    def test_day_of_year_2016_12_31(self):
        self.assertEqual(DateUtil.day_of_year(2016, 12, 31), 366)

    def test_day_of_year_2015_12_31(self):
        self.assertEqual(DateUtil.day_of_year(2015, 12, 31), 365)

    def test_day_of_year_2100_12_31(self):
        self.assertEqual(DateUtil.day_of_year(2100, 12, 31), 365)

    def test_day_of_year_2400_12_31(self):
        self.assertEqual(DateUtil.day_of_year(2400, 12, 31), 366)


if __name__ == '__main__':
    unittest.main()
