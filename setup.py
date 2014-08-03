#!/usr/bin/env python
from setuptools import setup
import re
import sys

requires = []

setup(
    name="yaragen",
    version='0.1.0',
    py_modules=['compare', 'yaragen', 'rulegen'],
    author="Adrian Maniatis",
    author_email="kwyjii@gmail.com",
    url="",
    description="Yara automated rule generator",
    long_description=open('README.rst').read(),
    license="ASL",
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires=requires
)

