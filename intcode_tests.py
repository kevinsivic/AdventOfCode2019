import unittest

from main import Computer


class MyTestCase(unittest.TestCase):
    def test_addition(self):
        comp = Computer()
        self.assertEqual([2, 0, 0, 0, 99], comp.compute([1, 0, 0, 0, 99]))

    def test_multiplication(self):
        comp = Computer()
        self.assertEqual([2, 3, 0, 6, 99], comp.compute([2, 3, 0, 3, 99]))


if __name__ == '__main__':
    unittest.main()
