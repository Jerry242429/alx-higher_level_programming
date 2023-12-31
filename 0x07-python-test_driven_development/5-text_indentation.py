#!/usr/bin/python3
"""
Module text_indentation adds two new lines after characters."""


def text_indentation(text):
    """Display text with added two newlines
    each of these characters {'.', '?', ':'}.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
