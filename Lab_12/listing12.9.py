def __radd__(self, param):
    """ Add two rasional (reverse)"""
    # mapping is reversed: if "1 + x", x maps to self, and 1 maps to f
    print('in radd')
    # mapping is already reversed so self will be rasional; call __add__
    return self.__add__(param)