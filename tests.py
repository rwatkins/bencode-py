import unittest
from unittest import TestCase

from bencode import encode


class IntegerTest(TestCase):
    def test_integer(self):
        self.assertEqual(encode(12), 'i12e')


if __name__ == '__main__':
    unittest.main()
