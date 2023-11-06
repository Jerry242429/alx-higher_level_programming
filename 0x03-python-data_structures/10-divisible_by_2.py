#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    list1 = []
    for x in my_list:
        if (x % 2) == 0:
            list1.append(True)
        else:
            list1.append(False)
    return list1
