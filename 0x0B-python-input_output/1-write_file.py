#!/usr/bin/python3
"""
This script demonstrates writing content to a text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns
    the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text content to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding='utf-8') as file:
        num_char = file.write(text)
        return num_char
