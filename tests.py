import unittest
from unittest import TestCase

from bencode import encode


class EncodeIntegerTest(TestCase):
    def test_integer(self):
        self.assertEqual(encode(12), 'i12e')

    def test_negative(self):
        self.assertEqual(encode(-12), 'i-12e')


class EncodeStringTest(TestCase):
    def test_string(self):
        self.assertEqual(encode('Hello'), '5:Hello')


class EncodeListTest(TestCase):
    def test_list(self):
        self.assertEqual(encode([12, 'Hello']), 'li12e5:Helloe')


class EncodeDictTest(TestCase):
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
