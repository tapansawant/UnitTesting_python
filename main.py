import sys
import unittest


def add(x, y):
    return x + y


def checkDivisibleby7(x):
    if x % 7 == 0:
        return True
    else:
        return False


class CheckDivisible(unittest.TestCase):

    @unittest.skipUnless(sys.platform.startswith("darwin"), "requires windows")
    def test_case_divisible(self):
        x = 14
        result = checkDivisibleby7(x)
        self.assertTrue(result)

    @unittest.skip("skipped....")
    def test_case_not_divisible(self):
        x = 9
        result = checkDivisibleby7(x)
        self.assertFalse(result)


class MyApp(unittest.TestCase):

    def test_case1(self):
        a = 10
        b = 22
        result = add(a, b)
        self.assertEqual(a + b, result)

    def test_case2(self):
        a = 12.5
        b = 12.9
        result = add(a, b)
        self.assertEqual(a + b, result)


if __name__ == "__main__":
    unittest.main()
