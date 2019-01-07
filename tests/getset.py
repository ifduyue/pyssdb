from . import TestCase

class TestGetSet(TestCase):
    def test_get(self):
        self.assertEqual(None, self.get('None')) 

    def test_set(self):
        self.assertEqual(1, self.set('set', 'set'))
