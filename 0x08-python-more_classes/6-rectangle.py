#!/usr/bin/python3
"""Defines a clss Rectangle"""

class Rectangle:
    """
    defines properties of rectangle
    Attributes:
        width (int): width
        height (int): height
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """New instances of Rectangle created.
        Arguments:
            width (int, optional): width
            height (int, optional): height
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

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
        """Set property for width of rectangle.
        Arguments:
            value (int): width.
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
        """set property for height of rectangle.
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
        """Area of a rectangle calculated.
        Returns:
            int: area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """perimeter of a rectangle calculated.
        Returns:
            int: perimeter of the rectangle.
        """
        if self.__height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """Display the rectangle with the character # .

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

    def __repr__(self):
        """String representation of the rectangle are returned
        Returns:
            str: the rectangle representation.
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes an object of a class
        """
        print("{:s}".format("Bye rectangle..."))
        type(self).number_of_instances -= 1
