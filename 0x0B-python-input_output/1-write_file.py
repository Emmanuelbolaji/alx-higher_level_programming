#!/usr/bin/python3
def write_file(filename="", text=""):
    char_no = 0
    with open(filename, "w", encoding="utf-8") as file:
        char_no = file.write(text)
        return char_no
