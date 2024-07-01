#!/usr/bin/python3
"""A module that defines a rectangle"""


class Rectangle:
    """
    Represents a rectangle with a width and height.

    Attributes:
        width (int): Width of the rectangle. Must be a non-negative integer.
        height (int): Height of the rectangle. Must be a non-negative integer.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object.
        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If either `width` or `height` is not an integer.
            ValueError: If either `width` or `height` is negative.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Gets the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is negative.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The new height of the rectangle
.
        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        calculates the area of the rectangle

        Returns:
            int: the multiplication of the height by the integer
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle (2 * (width + height)).
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        The rectangle is represented by '#' characters repeated to form
        the width and height of the rectangle. Each row is separated by
        a newline character.

         Returns:
             str: A string representation of the rectangle. If either the
                 width or height is 0, an empty string is returned.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""
        for i in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return rectangle_str
