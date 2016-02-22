import unittest


class TestAppCore(unittest.TestCase):
    """
    Test cases for AppCore module
    """
    # Initialization logic for the test suite declared in the test module
    # Code that is executed before all tests in one test run
    @classmethod
    def setUpClass(cls):
        pass

    # Clean up logic for the test suite declared in the test module
    # Code that is executed after all tests in one test run
    @classmethod
    def tearDownClass(cls):
        pass

    # Initialization logic
    # Code that is executed before each test
    def setUp(self):
        pass

    # Clean up logic
    # Code that is executed after each test
    def tearDown(self):
        pass

    def test_dummy(self):
        """
        Basic dummy test
        """
        self.assertTrue(False)


def suite():
    test = unittest.TestSuite()
    test.addTest(unittest.makeSuite(TestAppCore, 'TestAppCore'))
    return test


if __name__ == '__main__':
    unittest.main()