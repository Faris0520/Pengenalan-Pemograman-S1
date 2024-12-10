class MyClass(object):
    def __init__(self, param1=0):
        print('in constructor')
        self.value = param1

    def __str__(self):
        print('in str')
        return 'Val is: {}'.format(str(self.value))
    
    def __add__(self, param2):
        print('in add')
        result = self.value + param2.value
        return MyClass(result)