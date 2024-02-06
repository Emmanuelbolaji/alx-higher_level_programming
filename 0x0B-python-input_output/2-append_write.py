#!/usr/bin/python3
def append_write(filename="", text=""):
    char_no = 0
    with open(filename, "a", encoding='utf-8') as file:
        char_no = file.write(text)
        return char_no
