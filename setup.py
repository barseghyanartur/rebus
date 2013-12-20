import sys
import os
from setuptools import setup, find_packages

try:
    readme = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
except:
    readme = ''

version = '0.1'

install_requires = [
    'six>=1.1.0',
]

try:
    PY2 = sys.version_info[0] == 2
    PY3 = sys.version_info[0] == 3
    if PY2:
        pass
except:
    pass

setup(
    name = 'rebus',
    version = version,
    description = ("rebus - Generate base64-encoded strings consisting of alphanumeric symbols only."),
    long_description = readme,
    classifiers = [
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Environment :: Web Environment",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Text Processing",
        "Development Status :: 4 - Beta",
    ],
    keywords = 'b32encode, b64encode',
    author = 'Artur Barseghyan',
    author_email = 'artur.barseghyan@gmail.com',
    url = 'https://github.com/barseghyanartur/rebus/',
    package_dir = {'':'src'},
    packages = find_packages(where='./src'),
    license = 'GPL 2.0/LGPL 2.1',
    install_requires = install_requires,
    package_data = {
        'rebus': []
    },
    include_package_data = True,
)
