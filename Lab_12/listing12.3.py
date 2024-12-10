class Rasional(object):
    def __init__(self, numer, denom=1):
        print("in constructor")
        self.numer = numer
        self.denom = denom

    def __str__ (self):
        print('in str')
        return str(self.numer) + '/' + str(self.denom)
    
    def __repr__(self):
        print('in repr')
        return self.__str__()