
import six

__author__ = 'Daniel'


class Meta(type):
    def __new__(mcs, name, bases, class_dict):
        
        print (mcs, name, bases, class_dict)
        return type.__new__(mcs, name, bases, class_dict)


class MyClass(object):
    __metaclass__ = Meta
    foo = 1

    def __init__(self):
        self.bar = 2

    def foo_method(self):
        pass




registry = {}


def register_class(target_class):
    registry[target_class.__name__] = target_class


class RegistryMeta(type):
    
    def __new__(mcs, name, bases, class_dict):
        cls = type.__new__(mcs, name, bases, class_dict)
        register_class(cls)
        return cls


class RegisteredClass(six.with_metaclass(RegistryMeta)):
    pass
