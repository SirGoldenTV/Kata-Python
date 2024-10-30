from binaire_to_int import bin2int
import unittest


class TestStringsEnds(unittest.TestCase):

    def test_basic_test_cases(self):
        self.assertEqual(bin2int([0,0,0,1]), 1)
        self.assertEqual(bin2int([0,0,1,0]), 2)
        self.assertEqual(bin2int([1,1,1,1]), 15)
        self.assertEqual(bin2int([0,1,1,0]), 6)

if __name__ == '__main__':
    unittest.main()