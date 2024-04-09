#!/usr/bin/python3
""" a module """
class BaseGeometry:
    def area(self):
        raise Exception('area() is not implemented')
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError('<name> must be an integer')
        if value <= 0:
            raise ValueError('<name> must be greater than 0')

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)