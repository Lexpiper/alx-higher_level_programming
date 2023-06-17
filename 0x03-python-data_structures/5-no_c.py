#!/usr/bin/python3

def no_c(my_string):
    my_str = ""
    i = 0

    while i < len(my_string):
        if my_string[i] != 'c' and my_string[i] != 'C':
            my_str = my_string[i]
            return my_str
