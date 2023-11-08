#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list1= list(a_dictionary.keys())

    for k in list1:
        if value == a_dictionary[k]:
            del a_dictionary[k]

    return (a_dictionary)
