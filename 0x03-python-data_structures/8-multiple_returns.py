#!/usr/bin/python3

def multiple_returns(sentence):
    tuple_len = len(sentence)
    if sentence == "":
        return tuple_len, None
    else:
        return tuple_len, sentence[0]
