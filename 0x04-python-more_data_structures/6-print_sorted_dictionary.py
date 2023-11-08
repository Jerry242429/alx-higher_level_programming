#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for ke in sorted(a_dictionary.keys()):
        print("{}: {}".format(ke, a_dictionary[ke]))
