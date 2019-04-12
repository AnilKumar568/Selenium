import unittest


# After importing modules create 2 whitespaces. Similarly after creating a class 2 whitespaces need to be left
class Test(unittest.TestCase):  # Inheriting unittest.TestCase
    def test_firstTc(self):  # Always begin a method with test in unittest
        print("This is my 1st unit TC")


if __name__ == "__main__":
    unittest.main()

