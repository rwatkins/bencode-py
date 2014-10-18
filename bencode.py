def encode(value):
    if isinstance(value, int):
        return 'i%se' % value
