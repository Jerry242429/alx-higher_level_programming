#!/usr/bin/python3
"""this a module for base circle"""

class Base:
    """that represnts the base of our code"""
    __nb_objects = 0 
    def __init__(self, id=None):
        """one of the constructors"""
        if id is not None:
            self.id  = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
