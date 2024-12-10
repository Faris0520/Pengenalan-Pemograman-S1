def gcd(bigger, smaller):
    print('in gcd')
    if not bigger > smaller:
        bigger, smaller = smaller, bigger 
    while smaller != 0:
        remainder = bigger % smaller
        # print('calculation, big:{}, small: {}, rem{}'.\
        #       format(bigger, smaller, remainder)) # debugging
        bigger, smaller = smaller, remainder
    return bigger

def lcm(a,b):
    """Calculate the lowest common multiple of two positive integers."""
    print('in lcm')
    return (a*b)//gcd(a,b)

class Rasional(object):
    """Rational with numerator and denominator. Denominator parameter defaults to 1"""
    def __init__(self, numer, denom=1):
        print('in constructor')
        self.numer = numer
        self.denom = denom

    def __str__(self):
        """String representation for prrinting."""
        print('in str')
        return str(self.numer) + '/' + str(self.denom)
    
    def __repr__(self):
        """Used in interpreter. Call __str__ for now"""
        print('in repr')
        return self.__str__()
    
    def __add__(self, param_Rasional):
        """Add two rasionals"""
        print('in add')
        # find a common denominator (lcm)
        the_lcm = lcm(self.denom, param_Rasional.denom)
        # multiply each by the lcm, then add
        numerator_sum = (the_lcm * self.numer/self.denom) + \
                        (the_lcm * param_Rasional.numer/param_Rasional.denom)
        return Rasional(int(numerator_sum), the_lcm)
    
    def __sub__(self, param_Rasional):
        """Subtract two rasionals"""
        print('in sub')
        # subtraction is the same but with '-' instead of '+'
        the_lcm = lcm(self.denom, param_Rasional.denom)
        numerator_diff = (the_lcm * self.numer/self.denom) - \
                        (the_lcm * param_Rasional.numer/param_Rasional.denom)
        return Rasional(int(numerator_diff), the_lcm)