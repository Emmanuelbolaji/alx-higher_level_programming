#!/usr/bin/python3
"""
This script demonstrates reading content from a file.
"""


def read_file(filename=""):
    """
    Reads the contents of the specified file and prints
    it to the console

    Args:
        filename (str): The name of the file to be read.
        Defaults to an empty string.

    Returns:
       None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
