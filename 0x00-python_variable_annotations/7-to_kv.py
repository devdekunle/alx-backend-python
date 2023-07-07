#!/usr/bin/env python3
"""
    Desc:
         a type-annotated function to_kv that takes a string k
         and an int OR float v as arguments and returns a tuple.
         The first element of the tuple is the string k.
         The second element is the square of the int/float v
         and should be annotated as a float
    Args:
        k: str
        v: int or float
    Return: tuple
"""
from typing import List, Union, Optional, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    return a tuple
    """
    return (k, v ** 2)
