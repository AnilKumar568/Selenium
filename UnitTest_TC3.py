import unittest


# Execution will be in Alphabetical Order
def setUpModule():
    print("Executes only once when the Module is started")

def tearDownModule():
    print("Executes only once after the Module is executed")

class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("Start of SetUp method")


    @classmethod
    def tearDown(self):
        print("End of TearDown Method")

    @classmethod
    def setUpClass(cls):
        print("Setup Class executed only once before execution of other methods\n")

    @classmethod
    def tearDownClass(cls):
        print("Teardown class executed only once after completion of execution of other methods")

    def test_Search(self):
        print("This is a Search Test")

    def test_AdvSearch(self):
        print("This is a Adv Search")

    def test_NameSearch(self):
        print("This is a Search by Name")

    def test_IDSearch(self):
        print("This is a search by ID")


if __name__ == "__main__":
    unittest.main()

