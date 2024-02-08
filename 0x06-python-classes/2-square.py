#!/usr/bin/python3
"""module for a square"""


class Square:
    """ A class that defines a square """
    def __init__(self, size=0):
        """Define the size attribute.

        Args:
            size: the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
