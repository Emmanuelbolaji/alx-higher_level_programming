#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    sorted_dico = sorted(a_dictionary.items())
    if key in sorted_dico:
        sorted_dico[key] = value
        for key, value in sorted_dico.items():
            print(f"{key}: {value}")
    else:
        sorted_dico[key] = value
        for key, value in sorted_dico():
            print(f"{key}: {value}")
