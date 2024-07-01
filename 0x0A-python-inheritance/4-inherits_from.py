#!/usr/bin/python
"""
Module: inheritance_check

A module that provides a function `inherits_from`
to check if an object
inherits directly or indirectly from a specified class.

Functions:
- inherits_from(obj, a_class): Checks if geminiithe object `obj`
inherits directly or indirectly from `a_class`.
"""


def inherits_from(obj, a_class):
    """
    Checks if the object `obj` inherits directly or indirectly from `a_class`.

    Args:
    - obj: The object to check.
    - a_class: The class or type to compare against.

    Returns:
        - True if `obj` inherits directly or
        indirectly from `a_class`, False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
