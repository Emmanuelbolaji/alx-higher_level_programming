#!/usr/bin/python3
def no_c(my_string):
    target_1 = "c"
    target_2 = "C"
    new_string = ""
    for char in my_string:
        if char != target_1 or target_2:
            new_string = new_string + char
        return new_string
