#!/usr/bin/python3
"""
Module: type_checking
A module that provides functions for type checking operations.

Functions:
- is_kind_of_class(obj, a_class): Checks if the object `obj`
is an instance or subclass instance of `a_class`
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object `obj` is an instance or subclass
    instance of `a_class`.

    Args:
    - a_class: The class or type to compare against.

    Returns:
    - True if `obj` is an instance or subclass instance of
    `a_class`, False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    else:
        False
