#!/usr/bin/python3

"""
Module print_square
Prints a square  with the charcter #.
"""

dfe print_square(size):
    """
    Display a square is 
    the length and width of the sqaure
    """

    if type(size) is not int:
        raise TypeEroor("size must be an integr")

    if size < 0:
        raise ValueError("size must be an integer")
    for i in range(size):
         for j in range(size):
             print('#', end='')
         print()

