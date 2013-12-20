from __future__ import print_function

__title__ = 'rebus'
__version__ = '0.2'
__build__ = 0x000002
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'encode', 'b32encode', 'b64encode', 'urlsafe_b64encode',
    'decode', 'b32decode', 'b64decode', 'urlsafe_b64decode',
    )

import logging
import base64

from six import binary_type, PY3

from rebus.defaults import DEFAULT_SUFFIX

logger = logging.getLogger(__file__)

# ********************************************************
# ********************** Encoding ************************
# ********************************************************

class EncodedText(object):
    """
    Container.
    """
    def __init__(self, text, encoded):
        self.text = text
        self.encoded = encoded

    def __str__(self):
        return str(self.encoded)
    __unicode__ = __str__
    __repr__ = __str__


def encode(encoder, step, text, return_object=False):
    """
    :param callable encoder:
    :param int step:
    :param string text:
    :param bool return_object:
    :return string:
    """
    changed_text = binary_type((text + ((int(len(text) / step) + 1) * step - len(text)) * DEFAULT_SUFFIX).encode())
    encoded_text = encoder(changed_text)
    if return_object:
        return EncodedText(text=changed_text, encoded=encoded_text)
    return encoded_text

def b32encode(text, return_object=False):
    """
    :param string text:
    :param bool return_object:
    :return string:
    """
    return encode(base64.b32encode, 5, text, return_object=return_object)

def b64encode(text, return_object=False):
    """
    :param string text:
    :param bool return_object:
    :return string:
    """
    return encode(base64.b64encode, 3, text, return_object=return_object)

def urlsafe_b64encode(text, return_object=False):
    """
    :param string text:
    :param bool return_object:
    :return string:
    """
    return encode(base64.urlsafe_b64encode, 3, text, return_object=return_object)

# ********************************************************
# ********************** Decoding ************************
# ********************************************************

class DecodedText(object):
    """
    Container.
    """
    def __init__(self, text, decoded):
        self.text = text
        self.decoded = decoded

    def __str__(self):
        return str(self.decoded)
    __unicode__ = __str__
    __repr__ = __str__


def decode(decoder, text, return_object=False):
    """
    :param callable decoder:
    :param string text:
    :param bool return_object:
    :return string:
    """
    decoded_text = decoder(text.decode()).decode().replace(DEFAULT_SUFFIX, '')

    if return_object:
        return DecodedText(text=text, decoded=decoded_text)
    return decoded_text

def b32decode(text, return_object=False):
    """
    :param string text:
    :param bool return_object:
    :return string:
    """
    return decode(base64.b32decode, text, return_object=return_object)

def b64decode(text, return_object=False):
    """
    :param string text:
    :param bool return_object:
    :return string:
    """
    return decode(base64.b64decode, text, return_object=return_object)

def urlsafe_b64decode(text, return_object=False):
    """
    :param string text:
    :param bool return_object:
    :return string:
    """
    if PY3:
        text = text.decode()

    decoded_text = base64.urlsafe_b64decode(text)

    if PY3:
        decoded_text = decoded_text.decode()

    decoded_text = decoded_text.replace(DEFAULT_SUFFIX, '')

    if return_object:
        return DecodedText(text=text, decoded=decoded_text)
    return decoded_text
