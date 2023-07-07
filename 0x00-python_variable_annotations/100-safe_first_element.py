#!/usr/bin/env python3
"""
    Desc:
        Annotate a function - safe_first_element
    Args: lst
    Return: None or any
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    returns None or any data type
    """
    if lst:
        return lst[0]
    else:
        return None
