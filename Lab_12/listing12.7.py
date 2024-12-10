def reduce_rasional(self):
    """Return the reduced fractional value as a rasional"""
    print('in reduce')
    # find the gcd and then divide numnerator and demnominator by gcd
    the_gcd = gcd(self.numer//self.denom)
    return Rasional(self.numer//the_gcd, self.denom//the_gcd)

def __eq__(self, param_Rasional):
    """Compare two rasional for equality, return boolean"""
    print('in eq')
    # reduce both; then check that numerators and denominators are equal
    reduced_self = self.reduce_rasional()
    reduced_param = param_Rasional.reduce_rasional()
    return reduced_self.numer == reduced_param.numer and \
        reduced_self.denom == reduced_param.denom