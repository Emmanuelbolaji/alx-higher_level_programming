#!/usr/bin/python3i
"""
This module provides a function to look up attributes and methods of objects.

It contains a single function, lookup(), which returns a list of
available attributes and methods for any given Python object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
       obj: Any Python object

    Returns:
        list: A list of strings representing the names of
        attributes and methods
            available for the object.
    """
    return dir(obj)
