#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = my_list[:]
    for i in new_list:
        if i % 2 != 0:
            return new_list, False
        else:
            return new_list, True
