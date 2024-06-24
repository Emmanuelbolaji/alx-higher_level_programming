#!/usr/bin/python3

def element_at(my_list, idx):
    index_length = len(my_list)
    index = my_list[idx]
    if idx < 0:
        return None
    elif idx > index_length:
        return None
    else:
        return index
