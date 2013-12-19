===============================================
rebus
===============================================
Generate base-encoded strings consisting of alphanumeric symbols only.

Why did I make this app?
===============================================
Recently I have been working on implementing of a Google Authenticator app for
Plone (which I did for my beloved company - Goldmund, Wyldebeast & Wunderliebe).

For generating of a bar code image, I needed a base32 encoded string. While Android
devices could perfectly scan all bar-code image that I would generate, Apple devices
would raise errors on bar code images which were generated using strings that contain
one or more "=" characters.

The solution found was to add a number of \n at the end of the string to be encoded.

If you happen to experience similar problems, you know what to do.

Prerequisites
===============================================
- Python 2.6.8+, 2.7.+, 3.3.+

Installation
===============================================
Install latest stable version from PyPI:

    $ pip install rebus

...or latest stable version from GitHub:

    $ pip install -e git+https://github.com/barseghyanartur/rebus@stable#egg=rebus

...or latest stable version from BitBucket:

    $ pip install -e hg+https://bitbucket.org/barseghyanartur/rebus@stable#egg=rebus


Usage and examples
===============================================
Using `rebus` is damn easy. Whenever you would want to use base64.b32encode or base64.b64encode,
replace base64 with rebus.

Required imports.

>>> import rebus

b32encode string

>>> rebus.b32encode('abcdefg')
'MFRGGZDFMZTQUCQK'

b64encode string

>>> rebus.b64encode('abcdefg')
'YWJjZGVmZwoK'

urlsafe_b64encode

>>> rebus.urlsafe_b64encode('abcdefg')
'YWJjZGVmZwoK'

License
===============================================
GPL 2.0/LGPL 2.1

Support
===============================================
For any issues contact me at the e-mail given in the `Author` section.

Author
===============================================
Artur Barseghyan <artur.barseghyan@gmail.com>

Documentation!
=================================

Contents:

.. toctree::
   :maxdepth: 20

   rebus

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
