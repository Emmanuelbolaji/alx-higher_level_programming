#!/usr/bin/python3
"""
module that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file
    (UTF8) and returns the number of characters added.

    :param filename: Name of the file to append to.
    :param text: String to append to the file.
    :return: Number of characters added.
    """
    with open(filename, "a", encoding='utf-8') as file:
        num_char = file.write(text)
        return num_char
