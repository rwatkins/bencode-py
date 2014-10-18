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


class DictTest(TestCase):
    def test_dict(self):
        self.assertEqual(
            encode({
                'name': 'Riley',
                'ages': [26, 27],
                'parent': {
                    'name': 'Scott',
                },
            }),
            'd4:agesli26ei27ee4:name5:Riley6:parentd4:name5:Scottee')


if __name__ == '__main__':
    unittest.main()
