import unittest

class TestSum(unittest.TestCase):

    def test_sum1(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum2(self):
        self.assertEqual(sum([1, 2, 4]), 7, "Should be 6")

if __name__ == '__main__':
    unittest.main()
