import unittest

class LgmtTest(unittest.TestCase):
    def test_lgtm(self):
        from lgtm.core import lgtm
        self.assertIsNone(lgtm('./python.jpeg', 'LGTM'))