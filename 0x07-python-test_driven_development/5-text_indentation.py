#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        print(text, end=" ")
        if text in ['.', '?', ':']:
            print('\n\n')

