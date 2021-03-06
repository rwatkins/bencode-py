import re


def encode(value):
    if isinstance(value, int):
        return 'i%se' % value
    elif isinstance(value, str):
        return '%s:%s' % (len(value), value)
    elif isinstance(value, (list, tuple)):
        return 'l%se' % (''.join(encode(v) for v in value))
    elif isinstance(value, dict):
        assert all(isinstance(k, str) for k in value.iterkeys())
        return 'd%se' % ''.join('%s%s' % (encode(k), encode(v))
                                for (k, v) in value.iteritems())


def parse_int(s, end=0):
    """
    i12e => 12
    """
    value = ''
    nextchar = s[end:end+1]
    assert nextchar == 'i'
    end += 1
    nextchar = s[end:end+1]
    while nextchar != 'e':
        if not nextchar:
            raise Exception('Parsing int. Unexpected end of string.')
        value += nextchar
        end += 1
        nextchar = s[end:end+1]
    try:
        return int(value), end
    except ValueError as e:
        raise ValueError(u'Parsing int. Found illegal character. %s' % e)


def parse_string(s, end=0):
    """
    5:Hello => 'Hello'
    """
    value = ''
    length_str = ''
    nextchar = s[end:end+1]
    assert re.match(r'\d', nextchar)
    # parse length
    while nextchar != ':':
        length_str += nextchar
        end += 1
        nextchar = s[end:end+1]
    try:
        length = int(length_str)
    except ValueError as e:
        raise Exception('Error parsing string length: %s' % e)
    end += 1
    value = s[end:end+length]
    return value, end + length - 1


def parse_list(s, end=0):
    """
    l5:Hello6:world!e => ['Hello', 'world!']
    """
    nextchar = s[end:end+1]
    assert nextchar == 'l'
    end += 1
    nextchar = s[end:end+1]
    lst = []
    while nextchar != 'e':
        value, end = _decode(s, end=end)
        lst.append(value)
        end += 1
        nextchar = s[end:end+1]
    return lst, end


def parse_dict(s, end=0):
    """
    d5:wordsl5:Hello6:world!ee => {'words': ['Hello', 'world!']}
    """
    nextchar = s[end:end+1]
    assert nextchar == 'd'
    end += 1
    nextchar = s[end:end+1]
    obj = {}
    while nextchar != 'e':
        # parse key
        key, end = parse_string(s, end=end)
        end += 1
        # parse value
        value, end = _decode(s, end=end)
        obj[key] = value
        end += 1
        nextchar = s[end:end+1]
    return obj, end


def _decode(s, end=0):
    if not s:
        raise Exception('s is empty')

    nextchar = s[end:end+1]
    # Find value based on what it starts with
    if nextchar == 'i':
        value, end = parse_int(s, end=end)
    elif re.match(r'\d', nextchar):
        value, end = parse_string(s, end=end)
    elif nextchar == 'l':
        value, end = parse_list(s, end=end)
    elif nextchar == 'd':
        value, end = parse_dict(s, end=end)
    else:
        raise Exception("Don't know how to decode value beginning with %s"
                        % nextchar)
    return value, end


def decode(s):
    return _decode(s, end=0)[0]
