#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """
    Define properties of rectangle 
    Attributes:
        width (int): width
        height (int): height 
    """
    def __init__(self, width=0, height=0):
        """New instances of Rectangle created.
        Arguments:
            width (int, optional): width of rectangle
            height (int, optional): height of rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Width retriver.

        Returns:
            int: the width
        """
        return self.__width

    @property
    def height(self):
        """Height retriver.

        Returns:
            int: the height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Sets property for width of rectangle.
        Args:
            value (int): width

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Set property for height of rectangle.
        Arguments:
            value (int): height
        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """That calculates area of a rectangle.
        Returns:
            int: area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """That Calculates perimeter of a rectangle

        Returns:
            int: perimeter of the rectangle.
        """
        if self.__height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """display the rectangle with the character # .
        Returns:
            str: the rectangle
        """
        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append("#")
            rectangle.append("\n")

        rectangle.pop()

        return "".join(rectangle)
