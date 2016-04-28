
from __future__ import print_function

import sys
import os

# append module root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_bencode_int():
    from fenbu import bencode

    assert b'i0e' == bencode(0)
    assert b'i5e' == bencode(5)
    assert b'i-5e' == bencode(-5)
    assert b'i42e' == bencode(42)
    assert b'i-42e' == bencode(-42)
    assert b'i4294967296e' == bencode(2**32)
    assert b'i-4294967296e' == bencode(-2**32)

def test_bencode_str():
    from fenbu import bencode

    assert b'1:e' == bencode('e')

def test_bencode_list():
    from fenbu import bencode

    assert b'le' == bencode(list())
    assert b'li32e3:foode3:bare' == bencode([32, 'foo', {}, 'bar'])

def test_bencode_dict():
    from fenbu import bencode

    assert b'de' == bencode(dict())
    assert b'd2:AAi3e2:aai1e2:bbi2ee' == bencode({'aa': 1, 'bb': 2, 'AA': 3})


if __name__ == '__main__':
    test_bencode_int()
    test_bencode_str()
    test_bencode_list()
    test_bencode_dict()

