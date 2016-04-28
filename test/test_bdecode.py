
from __future__ import print_function

import sys
import os

# append module root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_bdecode_int():
    from fenbu import bdecode

    assert bdecode('i0e') == int(0)
    assert bdecode('i1e') == int(1)
    assert bdecode('i42e') == int(42)
    assert bdecode('i-2e') == int(-2)
    assert bdecode('i-42e') == int(-42)
    assert bdecode('i4294967296e') == int(2**32)
    assert bdecode('i-4294967296e') == int(-2**32)

def test_bdecode_str():
    from fenbu import bdecode

    assert bdecode('1:e') == bytes('e')
    assert bdecode('3:foo') == bytes('foo')

def test_bdecode_list():
    from fenbu import bdecode


def test_bdecode_dict():
    from fenbu import bdecode


if __name__ == '__main__':
    test_bdecode_int()
    test_bdecode_str()
    test_bdecode_list()
    test_bdecode_dict()

