
def bdecode(b):
    """
    Convert a bencoded byes sequence into a tree of dict, list, int and str.
    """
    result = None
    stack = []

    key = None
    val = None

    k = 0
    while k < len(b):
        if b[k] == 'i':
            k += 1
            epos = b.find('e', k)
            val = int(b[k:epos])
            k = epos+1
        elif b[k] in '0123456789':
            sz = 0
            while b[k] in '0123456789':
                sz = sz * 10 + int(b[k])
                k += 1
            if b[k] != ':':
                raise TypeError('bencoded data is not valid.')
            k += 1
            val = b[k:k+sz]
            k += sz
            if len(stack) != 0 and key is None and isinstance(stack[-1], dict):
                key = val
                continue
        elif b[k] == 'l':
            val = list()
            k += 1
        elif b[k] == 'd':
            val = dict()
            k += 1
        # handle end of list or dict
        elif b[k] == 'e':
            stack.pop()
        else:
            raise TypeError('bencoded data is not valid.')

        if len(stack) == 0:
            stack.append(val)
        elif isinstance(stack[-1], dict):
            stack[-1][key] = val
        elif isinstance(stack[-1], dict):
            stack[-1].append(val)
        else:
            pass

        key = None
        val = None

    if len(stack) != 1:
        raise TypeError('bencoded data is not valid.')

    return stack[-1]

