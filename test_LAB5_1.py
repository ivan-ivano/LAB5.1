import unittest
from LAB5_1 import h


class TestH(unittest.TestCase):
    def test_h(self):
        self.assertEqual(h(2, 3), 0.16216216216216217)  # add assertion here
