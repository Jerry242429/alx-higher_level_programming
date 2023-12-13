#!/usr/bin/python3
"""Modules for square class"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Defines properties of Square."""
    def __init__(self, size, x=0, y=0, id=None):
        """Creates new objects."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Display string info about this square"""
        return ("[Square] ({}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y, self.size))
