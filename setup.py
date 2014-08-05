#!/usr/bin/env python
from setuptools import setup
import re
import sys

requires = ['yara', 'begins']

setup(
    name="yaragen",
    version='0.1.1',
    packages=['yaragen', 'yaragen.rulegens'],
    author="Adrian Maniatis",
    author_email="kwyjii@gmail.com",
    url="https://github.com/JoeyJoJoJrShabadu/yaragen",
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
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires=requires
)

