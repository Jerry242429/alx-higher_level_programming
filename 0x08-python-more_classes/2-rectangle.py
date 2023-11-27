#!/usr/bin/python3
"""Defines a class Rectangle"""

class Rectangle:
    """
    defines properties of rectangle by: (based on 1-rectangle.py).
    Attributes:
        width (int): width 
        height (int): height
    """
    def __init__(self, width=0, height=0):
        """Used to creates new instances of Rectangle.
        Arguments:
            width (int, optional): width
            height (int, optional): height
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Width retriver.
        Returns:
            int: width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """Height retriver.
        Returns:
            int: height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Property setter for width of rectangle.
        Arguments:
            value (int): width of the rectangle.

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
        """Property setter for height of recyangle.
        Args:
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
        """Perform and Calculates perimeter of a rectangle
        Returns:
            int: perimeter of the rectangle.
        """
        if self.__height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)
