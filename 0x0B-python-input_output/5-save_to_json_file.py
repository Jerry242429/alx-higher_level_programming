#!/usr/bin/python3
'''
functions:
-> save_to_json_file
'''
import json
def save_to_json_file(my_obj, filename):
    ''' Object writtes to a text file, using JSON representation '''

    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
