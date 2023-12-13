#!/usr/bin/python3
"""Module that define class of circle"""

from inspect import classify_class_attrs
from models.rectangle import Rectangle

class Square(Rectangle):
    """Class that defines properties of Square."""
    def __init__(self, size, x=0, y=0, id=None):
        """Creates new instances of Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string square"""
        return ("[Square] ({}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """size of this square"""
        return self.width

    @size.setter
    def size(self, value):
        """Property setter for width of square."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute

        Args:
            *args (tuple): arguments.
            **kwargs (dict): double pointer to a dictionary.
        """
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)
    def to_dictionary(self):
        """Returns the dictionary representation of a Square.

        Returns:
            dict: square.
        """
        dict1 = self.__dict__
        dict2 = {}
        dict2['id'] = dict1['id']
        dict2['size'] = dict1['_Rectangle__width']
        dict2['x'] = dict1['_Rectangle__x']
        dict2['y'] = dict1['_Rectangle__y']

        return dict2
