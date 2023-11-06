#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    list1 = my_list.copy()
    list1.sort()
    return list1[-1]
