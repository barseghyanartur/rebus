from __future__ import print_function

__title__ = 'rebus'
__version__ = '0.1'
__build__ = 0x000001
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('b32encode', 'b64encode', 'urlsafe_b64encode')

import logging
import base64

from six import binary_type

logger = logging.getLogger(__file__)

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


def b32encode(text, return_object=False):
    """
    :param string text:
    :param bool return_object:
    :return string:
    """
    changed_text = binary_type((text + ((int(len(text) / 5) + 1) * 5 - len(text)) * '\n').encode())
    encoded_text = base64.b32encode(changed_text)
    if return_object:
        return EncodedText(text=changed_text, encoded=encoded_text)
    return encoded_text

def b64encode(text, return_object=False):
    """
    :param string text:
    :return string:
    """
    changed_text = binary_type((text + ((int(len(text) / 3) + 1) * 3 - len(text)) * '\n').encode())
    encoded_text = base64.b64encode(changed_text)
    if return_object:
        return EncodedText(text=changed_text, encoded=encoded_text)
    return encoded_text

def urlsafe_b64encode(text, return_object=False):
    """
    :param string text:
    :return string:
    """
    changed_text = binary_type((text + ((int(len(text) / 3) + 1) * 3 - len(text)) * '\n').encode())
    encoded_text = base64.urlsafe_b64encode(changed_text)
    if return_object:
        return EncodedText(text=changed_text, encoded=encoded_text)
    return encoded_text
