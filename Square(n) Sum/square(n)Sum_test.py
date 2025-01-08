import unittest
from squareSum import square_sum

class TestSquareSum(unittest.TestCase):
    def test_basic_cases(self):
        cases = [
            ([1, 2], 5),
            ([0, 3, 4, 5], 50),
            ([], 0),
            ([-1, -2], 5),
            ([-1, 0, 1], 2),
        ]
        for inputs, expected in cases:
            result = square_sum(inputs)
            print(f"Input: {inputs}, Expected: {expected}, Got: {result}")
            self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()