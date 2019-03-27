import unittest

class Testunittest(unittest.TestCase):
    def test_assert_eq(self):
        self.assertEqual(1,1,"不相等...")

    def test_assert_ne(self):
        self.assertNotEqual(1, 1, "相等...")