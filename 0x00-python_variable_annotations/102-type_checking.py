#!/usr/bin/env python3
"""
    Desc:
        Use mypy to validate the following piece of code
        and apply any necessary changes.
    Args:
        lst: Tuple,
        factor: int
    Return:
        Tuple
"""
from typing import Tuple, List, TYPE_CHECKING, Any, Union


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
        return a tuple after fixing annotations
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


if TYPE_CHECKING:
    array = (12, 72, 91)

    zoom_2x = zoom_array(array)

    zoom_3x = zoom_array(array, 3)
