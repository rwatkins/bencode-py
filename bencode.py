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
