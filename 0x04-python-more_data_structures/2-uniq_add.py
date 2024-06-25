#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq = set(my_list)
    my_new_list = list(uniq)
    total_sum = sum(my_new_list)
    return total_sum
