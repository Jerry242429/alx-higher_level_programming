#!/usr/bin/python3
def remove_char_at(str, n):
    wstr = ""
    for a, b in enumerate(str):
        if a != n:
            wstr += b
    return wstr
