#!/usr/bin/python3
def no_c(my_string):
    remove = ['c', 'C']
    result = ''.join(char for char in my_string if char not in remove)
    return result
