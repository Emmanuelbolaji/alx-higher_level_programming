#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns the number of characters added.

    :param filename: Name of the file to append to.
    :param text: String to append to the file.
    :return: Number of characters added.
    """
    char_no = 0
    with open(filename, "a", encoding='utf-8') as file:
        char_no = file.write(text)
        return char_no
