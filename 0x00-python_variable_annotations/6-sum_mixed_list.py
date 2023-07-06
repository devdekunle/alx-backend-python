#!/usr/bin/env python3
"""
    Desc:
        a type-annotated function sum_mixed_list which takes a list mxd_lst
        of integers and floats and returns their sum as a float.

    Args:
        mxd_lst: a list of integers and float

    Return:
        sum: float
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:

    """
        returns the sum of a list of floats and integer values
    """
    return sum(mxd_lst)
