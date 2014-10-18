def encode(value):
    if isinstance(value, int):
        return 'i%se' % value
    elif isinstance(value, str):
        return '%s:%s' % (len(value), value)
    elif isinstance(value, (list, tuple)):
        return 'l%se' % (''.join(encode(v) for v in value))
