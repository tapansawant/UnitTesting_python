import unittest


def biggestnumber(x, y):
    if (x > y):
        return "first"
    else:
        return "second"


class CheckBiggestNumber(unittest.TestCase):
    def test_case_firstone(self):
        x = 10
        y = 8
        result = biggestnumber(x, y)
        self.assertEqual("first", result)

    def test_case_secondone(self):
        x = 8
        y = 10
        result = biggestnumber(x, y)
        self.assertNotEqual("first", result)


if __name__ == "__main__":
    unittest.main()
