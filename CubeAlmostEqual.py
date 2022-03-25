import unittest

def VolmOfCube(a):
    return a*a*a


class CheckVolume(unittest.TestCase):
    def test_case(self):
        a = 5.5
        result = VolmOfCube(a)
        self.assertAlmostEqual(result, a*a*a)


if __name__ == "__main__":
    unittest.main()