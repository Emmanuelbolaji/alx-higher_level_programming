#!/usr/bin/python3
import json

def load_from_json_file(filename):
    with open(filename, "r") as file:
        python_obj = json.loads(file)
        rform = python_obj.read()
        return rform
