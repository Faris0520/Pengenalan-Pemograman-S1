class MyClass (object):
    class_attribute = 'world'

    def my_method(self, param1):
        print('\nHello {}'.format(param1))
        print('The object that called this method is: {}'.\
              format(str(self)))
        self.instance_attribute = param1

my_instance = MyClass()
print("output of dir(my_instance):")
print(dir(my_instance))
my_instance.my_method('world')
print("Instance has newa attribute with value: {}".\
      format(my_instance.instance_attribute))
print("Output of dir(my_instance):")
print(dir(my_instance))