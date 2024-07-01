#!/usr/bin/python3
"""
Module: is_same_class

A module that provides a function `is_same_class` to check if an object
is an instance of a specified class.

Functions:
- is_same_class(obj, a_class): Checks if the object `obj` is an instance
of the class `a_class`.
"""


def is_same_class(obj, a_class):
    """
    Checks if the object `obj` is an instance of the class `a_class`.

    Args:
    - obj: The object to check.
    - a_class: The class to compare against.

    Returns:
    - True if `obj` is an instance of `a_class`, False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    else:
        False
