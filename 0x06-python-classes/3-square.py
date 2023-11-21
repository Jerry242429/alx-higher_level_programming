#!/usr/bin/python3
"""Define a class Square."""
class Square:
    """Represent a Square."""
    def __init__(self, size=0):
        """Constructor.
    
        Args:
            size: Length of a side of the Square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
    def area(self):
        """Area of this Square

        Returns:
                The size squared.
        """
        return self.__size ** 2
