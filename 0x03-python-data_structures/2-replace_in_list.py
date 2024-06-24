#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    index_length = len(my_list)
    my_list[idx] = element
    if idx < 0:
        return my_list
    elif idx > index_length:
        return my_list
    else:
        return my_list[idx]
