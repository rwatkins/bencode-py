import unittest
from unittest import TestCase

from bencode import encode


class IntegerTest(TestCase):
    def test_integer(self):
        self.assertEqual(encode(12), 'i12e')


class StringTest(TestCase):
    def test_string(self):
        self.assertEqual(encode('Hello'), '5:Hello')


class ListTest(TestCase):
    def test_list(self):
        self.assertEqual(encode([12, 'Hello']), 'li12e5:Helloe')


if __name__ == '__main__':
    unittest.main()
