
import collections
import operator

def bencode(data):
    """
    Convert a hirarchical tree of dict, list, str, and int objects into bencoded bytes.
    """
    result = []
    stack = []
    stack.append(data)

    while stack:
        d = stack.pop()
        if isinstance(d, int):
            result.append('i')
            result.append(str(d))
            result.append('e')
        elif isinstance(d, str):
            s = bytes(d)
            result.append(str(len(s)))
            result.append(':')
            result.append(s)
        elif isinstance(d, list):
            stack.append(iter(d))
            result.append('l')
        # TODO: OrderedDict
        elif isinstance(d, dict):
            pairs = d.items()
            pairs.sort(key=operator.itemgetter(0))
            stack.append(iter(pairs))
            result.append('d')
        elif isinstance(d, collections.Iterable):
            try:
                x = next(d)
                stack.append(d)
                if isinstance(x, tuple):
                    # key value pair of a dict
                    stack.append(x[1]) # value
                    stack.append(x[0]) # key, processed next
                else:
                    # list item
                    stack.append(x) # value
            except StopIteration as e:
                result.append('e')
        else:
            raise TypeError('Unsupported type.')

    return b"".join(result)

