from __future__ import print_function

__title__ = 'rebus.tests'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

import unittest

from six import binary_type

import rebus

PRINT_INFO = True

def print_info(func):
    """
    Prints some useful info.
    """
    if not PRINT_INFO:
        return func

    def inner(self, *args, **kwargs):
        result = func(self, *args, **kwargs)

        print('\n\n%s' % func.__name__)
        print('============================')
        if func.__doc__:
            print('""" %s """' % func.__doc__.strip())
        print('----------------------------')
        if result is not None:
            print(result)
        print('\n++++++++++++++++++++++++++++')

        return result
    return inner

TEXTS = (
    'a',
    'ab',
    'abc',
    'abcd',
    'abcde',
    'abcdef',
    'abcdefg',
    'abcdefgh',
    'abcdefghi',
    'abcdefghij',
    'abcdefghijk',
    'abcdefghijkl',
    'abcdefghijklm',
    'abcdefghijklmn',
    'abcdefghijklmno',
    'abcdefghijklmnop',
    'abcdefghijklmnopq',
    'abcdefghijklmnopqr',
    'abcdefghijklmnopqrs',
    'abcdefghijklmnopqrst',
    'abcdefghijklmnopqrstu',
    'abcdefghijklmnopqrstuv',
    'abcdefghijklmnopqrstuvw',
    'abcdefghijklmnopqrstuvwx',
    'abcdefghijklmnopqrstuvwxy',
    'abcdefghijklmnopqrstuvwxyz',
)

class RebusEncodingTest(unittest.TestCase):
    """
    Encoding tests.
    """
    def setUp(self):
        self.texts = TEXTS
        self.equal_sign = binary_type('='.encode())

    def __encode(self, encoder):
        """
        :param callable encoder:
        :return list:
        """
        flow = []
        for text in self.texts:
            encoded_text = encoder(text)
            self.assertTrue(self.equal_sign not in encoded_text)
            flow.append((text, encoded_text))

        return flow

    @print_info
    def test_01_b32encode(self):
        """
        Test the ``rebus.b32encode``.
        """
        return self.__encode(rebus.b32encode)

    @print_info
    def test_02_b64encode(self):
        """
        Test the ``rebus.b64encode``.
        """
        return self.__encode(rebus.b64encode)

    @print_info
    def test_03_urlsafe_b64encode(self):
        """
        Test the ``rebus.urlsafe_b64encode``.
        """
        return self.__encode(rebus.urlsafe_b64encode)


class RebusDecodingTest(unittest.TestCase):
    """
    Decoding tests.
    """
    def setUp(self):
        self.texts = TEXTS
        self.equal_sign = binary_type('='.encode())

    def __decode(self, encoder, decoder):
        """
        :param callable encoder:
        :param callable decoder:
        :return list:
        """
        flow = []
        for text in self.texts:
            encoded_text = encoder(text)
            self.assertTrue(self.equal_sign not in encoded_text)
            decoded_text = decoder(encoded_text)
            self.assertTrue(decoded_text == text)
            flow.append((text, encoded_text, decoded_text))

        return flow

    @print_info
    def test_01_b32decode(self):
        """
        Test the ``rebus.b32decode``.
        """
        return self.__decode(rebus.b32encode, rebus.b32decode)

    @print_info
    def test_02_b64decode(self):
        """
        Test the ``rebus.b64decode``.
        """
        return self.__decode(rebus.b64encode, rebus.b64decode)

    @print_info
    def test_03_urlsafe_b64encode(self):
        """
        Test the ``rebus.urlsafe_b64decode``.
        """
        return self.__decode(rebus.urlsafe_b64encode, rebus.urlsafe_b64decode)


if __name__ == "__main__":
    # Tests
    unittest.main()
