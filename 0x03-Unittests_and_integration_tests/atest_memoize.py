#!/usr/bin/env python3
from typing import Callable
from functools import wraps




def memoize(f: Callable) -> Callable:
    attr_name = "_{}".format(f.__name__)

    @property
    @wraps(f)
    def memoized(self):
        """memoized wraps"""
        if not hasattr(self, attr_name):
            setattr(self, attr_name, f(self))
        return getattr(self, attr_name)

    return memoized

class MyClass:
    @memoize
    def a_method(self):
        print("a_method called")
        return 42


my_object = MyClass()
my_object.a_method
my_object.a_method
