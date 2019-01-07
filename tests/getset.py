import unittest

class TestGetSet(unittest.TestCase):
    def setUp(self):
        import pyssdb
        self.ssdb = pyssdb.Client()

    def tearDown(self):
        self.ssdb.disconnect()

    def test_get(self):
        self.assertEqual(None, self.get('None')) 

    def test_set(self):
        self.assertEqual(1, self.set('set', 'set'))
