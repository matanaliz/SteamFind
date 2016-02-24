import unittest
from stc import steamcore

class TestSteamCore(unittest.TestCase):
    """
    Testcases for SteamCore module
    """
    # Initialization logic for the test suite declared in the test module
    # Code that is executed before all tests in one test run
    @classmethod
    def setUpClass(cls):
        cls.steamid = '76561198044310785'

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

    def test_get_player(self):
        """
        Test for get-player function
        """
        # my steam id

        p = steamcore.get_player(self.steamid)
        self.assertTrue(p.steamid == self.steamid)
        self.assertTrue(p.name == 'Ben Stiller')
        self.assertTrue(p.avatar == 'https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/57/577a46a9f28d770adfc24a00acb0ab39bc35caa3.jpg')

    def test_get_owned_games(self):
        p = steamcore.get_player(self.steamid)
        games = steamcore.get_owned_games(p)
        self.assertTrue(games)


def suite():
    test = unittest.TestSuite()
    test.addTest(unittest.makeSuite(TestSteamCore, 'TestSteamCore'))
    return test


if __name__ == '__main__':
    unittest.main()
