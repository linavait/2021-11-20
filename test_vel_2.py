import unittest

from testvel import count_digits, count_zeros


class TestDigits(unittest.TestCase):
    def test_test_one_digit(self):
        self.assertEqual(count_digits(5), 1, msg = 'neteisingai')

    def test_two_digits(self):
        self.assertEqual(count_digits(55), 2)

    def test_many_digits(self):
        self.assertEqual(count_digits(111111111, 2)

    def test_false_input(self):
          with self.assertRaises(ValueError):
              count_digits("aaabb")


class TestZeroes(unittest.TestCase):


    def test_no_zeros(self):
        self.assertEqual(count_zeros(123), 0)

    def test_one_zeros(self):
        self.assertEqual(count_zeros(10), 1)

    def test_many_zeros(self):
        self.assertEqual(count_zeros(10000000000), 10)

    def test_only_zeros_as_int(self):
        self.assertEqual(count_zeros(0000), 3)


if __name__ == "__main__":

    unittest.main()