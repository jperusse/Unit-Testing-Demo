import unittest

from calc import Calculator


class CreateFirstTest(unittest.TestCase):
    def test_add(self):
        """
        Test add function from class Calculator
        """
        calcu = Calculator()
        result = calcu.add(3, 4)
        self.assertEqual(result, 7)


if __name__ == "__main__":
    unittest.main()
