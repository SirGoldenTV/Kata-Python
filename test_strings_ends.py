from strings_ends import solution
import unittest

fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)

fixed_tests_False = (
    ( "sumo",    "omo"   ),
    ( "samurai", "ra"    ),
    ( "abc",     "abcd"  ),
    ( "ails",    "fails" ),
    ( "this",    "fails" ),
    ( "spam",    "eggs"  )
)

class TestStringsEnds(unittest.TestCase):
    
    print("True Cases")
    def test_true_case(self):
        for text, ending in fixed_tests_True:
            with self.subTest(text = text, ending = ending):
                self.assertEqual(solution(text, ending), True)
    print("False Cases")
    def test_false_case(self):
        for text, ending in fixed_tests_False:
            with self.subTest(text = text, ending = ending):
                self.assertEqual(solution(text, ending), False)

if __name__ == '__main__':
    unittest.main()