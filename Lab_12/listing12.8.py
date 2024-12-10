def __add__(self, param):
    """Add two rasional. Allows int as a parameter"""
    print('in add')
    if type(param) == int: # convert int to rasional
        param = Rasional(param)
    if type(param) == Rasional:
        # find a common denominator (lcm)
        the_lcm = lcm(self.denom, param.denom)
        # multiply each by the lcm, then add
        numerator_sum = (the_lcm * self.numer/self.denom) + \
        (the_lcm * param.number/param.denom)
        return Rasional(int(numerator_sum), the_lcm)
    else:
        print('wrong type') # problem: some type we cannoot handle
        raise(TypeError)