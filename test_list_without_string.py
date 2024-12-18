from list_without_string import filter_list
import unittest

class TestStringsEnds(unittest.TestCase):

    def test_basic_examples(self):
        self.assertEqual(filter_list([1, 2, 'a', 'b']), [1, 2], 'For input [1, 2, "a", "b"]')
        self.assertEqual(filter_list([1, 'a', 'b', 0, 15]), [1, 0, 15], 'Fot input [1, "a", "b", 0, 15]')
        self.assertEqual(filter_list([1, 2, 'aasf', '1', '123', 123]), [1, 2, 123], 'For input [1, 2, "aasf", "1", "123", 123]')

if __name__ == '__main__':
    unittest.main()