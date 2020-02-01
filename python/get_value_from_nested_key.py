#!/usr/bin/env python

data = input("Enter the nested object: ")
list_in = input("Enter the key: ")

def get_nested(data, *args):
    if args and data:
        element  = args[0]
        if element:
            value = data.get(element)
            return value if len(args) == 1 else get_nested(value, *args[1:])

print(get_nested(data,list_in))