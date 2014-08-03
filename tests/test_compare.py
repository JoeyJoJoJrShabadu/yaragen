from __future__ import absolute_import
try:
    import unittest2 as unittest
except ImportError:
    import unittest
try:
    from inspect import signature
except ImportError:
    from funcsigs import signature
import sys

class TestConfig(unittest.TestCase):

    def test_print_config(self):
        pass