#!/usr/bin/env python3
"""
Given the parameters and the return values, add
type annotations to the function
"""
from typing import TypeVar, Union, Mapping, Any


T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, None] = None
        ) -> Union[Any, T]:
    """return valie of dict[key] or a default value"""
    if key in dct:
        return dct[key]
    else:
        return default
