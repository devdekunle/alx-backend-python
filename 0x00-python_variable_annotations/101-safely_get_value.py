#!/usr/bin/env python3
"""
    Desc:
        Add annotations to a function
    Args:
        dct: a Mapping
        key:    Any
        default: None
    Return:
        default or any
"""
from typing import Mapping, Union, Any, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
