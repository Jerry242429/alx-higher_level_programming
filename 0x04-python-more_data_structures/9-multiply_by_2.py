#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {y: (a_dictionary[y] * 2) for y in a_dictionary}
    return new
