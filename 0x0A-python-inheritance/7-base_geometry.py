#!/usr/bin/python3
"""
Module: base_geometry

A module that provides the base class `BaseGeometry`
for geometric operations.

Classes:
    - BaseGeometry: A base class for geometric operations.
"""


class BaseGeometry:
    """
    A base class for geometric operations.

    This class is intended to be used as a foundation
    for other geometric classes.
    Currently, it does not implement any methods or attributes.
    """
    def area(self):
        """
        Raises an exception indicating that the area method is not implemented

        This method should be overridden by subclasses
        to provide the actual area calculation.

        Raises:
        - Exception: Indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that `value` is a positive integer.

        Args:
        - name (str): The name of the value (assumed to be a string).
        - value (int): The value to validate.

        Raises:
        - TypeError: If `value` is not an integer.
        - ValueError: If `value` is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise TypeError(f"{name} must be greater than 0")
