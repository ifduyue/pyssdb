from . import TestCase

class TestGetSet(TestCase):
    def test_get(self):
        self.assertEqual(None, self.ssdb.get('None')) 

    def test_set(self):
        self.assertEqual(1, self.ssdb.set(b'set', b'set'))
        self.assertEqual(1, self.ssdb.set(b'set', b'set'))
        self.assertEqual(b'set', self.ssdb.get('set'))
