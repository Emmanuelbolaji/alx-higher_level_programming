#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    result = tuple(a + b for a, b in zip(tuple_a, tuple_b))
    return result
