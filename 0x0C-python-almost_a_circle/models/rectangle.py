#!/usr/bin/python3
"""
"""

from base import Base

class Rectangle(Base):
    """
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        
    @property
    def width(self):
        """
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        value = self.__width

    @property
    def height(self):
        """
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        value = self.__height


    @property
    def x(self):
        """
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        value = self.__x

    @property
    def y(self):
        """
        """
        return self.__y
    
    @y.setter
    def y(self, value):
        """
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if x < 0:
            raise ValueError("y must be >= 0")
        value = self.__y
