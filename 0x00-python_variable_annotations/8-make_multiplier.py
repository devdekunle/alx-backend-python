#!/usr/bin/env python3
"""
    Desc:
         a type-annotated function make_multiplier that takes a float
         multiplier as argument and returns a function that
         multiplies a float by multiplier.
    Args:
        multiplier: float
    Return:
        function: callable
"""
from typing import List, Tuple, Union, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a function that multiplies a float by a multiplier
    """
    def multiply(value: float) -> float:
        """
        return answer
        """
        return value * multiplier
    return multiply
