import unittest

from algoritmos.my_stack import MyStack


class TestCase(unittest.TestCase):

    def test_stack(self):
        numbers = MyStack()
        numbers.push(1)
        numbers.push(2)
        last_number = numbers.pop()
        self.assertEqual(last_number, 2, "Should be 2")
        contains_2 = numbers.contains(2)
        self.assertFalse(contains_2)


if __name__ == '__main__':
    unittest.main()
