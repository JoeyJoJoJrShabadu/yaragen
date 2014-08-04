from collections import namedtuple

_std_keys = ['rule', 'count']
AsciiStringRule = namedtuple('AsciiStringRule', _std_keys)
WideStringRule = namedtuple('WideStringRule', _std_keys)
WideAsciiStringRule = namedtuple('WideAsciiStringRule', _std_keys)
BinaryRule = namedtuple('BinaryRule', _std_keys)

