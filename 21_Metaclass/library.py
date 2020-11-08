# library.py

# class Base:
#     def bar(self):
#         return 'bar'


#how do you enforce a constaint in python from
# a base class to a derived class --> Metaclass

#with Metaclass
class BaseMeta(type):
    def __new__(cls, name, bases, body):
        if 'baz' not in body:
            raise TypeError()
        return super().__new__(cls, name, bases, body)

#1. alternativ
class Base:
     def bar(self):
         return self.baz()

#how abstract class is implemented?
#
'''
python runtime
>>>def f()    # you can create a function, that call a class :-O
    class Foo:
        pass

>>>from dis import dis
>>>dis(f)

'''
