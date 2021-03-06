#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(
    name = 'Spayify',
    version = '0.1a',
    description = 'Allows you to convert a spotify playlist in to MP3s you can buy.',
    author = 'Matt Copperwaite',
    author_email = 'matt@copperwaite.net',
    url = 'https://github.com/yamatt/spayify/',
    packages=[
        "spayify",
    ],
    install_requires = [
        "requests >= 2.5.3",
    ],
    license = "AGPLv3",
    classifiers = [
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3"
    ]
)
