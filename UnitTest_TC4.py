import unittest


class Apptesting(unittest.TestCase):
    @unittest.skip("I'm skipping this test method bcz it is not yet ready")
    def test_Search(self):
        print("This is a Search Test")

    @unittest.SkipTest
    def test_AdvSearch(self):
        print("This is a Adv Search")

    @unittest.skipIf(1 == 1, "This method got skipped bcz 1 is equal to 1")
    def test_NameSearch(self):
        print("This is a Search by Name")

    def test_IDSearch(self):
        print("This is a search by ID")


if __name__ == "__main__":
    unittest.main()


