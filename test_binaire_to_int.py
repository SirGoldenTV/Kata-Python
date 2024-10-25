from binaire_to_int import binary_array_to_number
import unittest


class TestStringsEnds(unittest.TestCase):

    def test_basic_test_cases(self):
        self.assertEqual(binary_array_to_number([0,0,0,1]), 1)
        self.assertEqual(binary_array_to_number([0,0,1,0]), 2)
        self.assertEqual(binary_array_to_number([1,1,1,1]), 15)
        self.assertEqual(binary_array_to_number([0,1,1,0]), 6)

if __name__ == '__main__':
    unittest.main()