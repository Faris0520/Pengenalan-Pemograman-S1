def lcm(a,b):
    """calculate the lowest common multiple of two positivie integers"""
    return (a*b)//gdc(a,b) # equation 12.1, ensure an int is returned