#!/usr/bin/env python3
"""
    Desc:
        Annotate a function’s parameters and
        return values with the appropriate types
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        takes in an iterable(list, tuple, set) and returns a list of tuples
    """
    return [(i, len(i)) for i in lst]
