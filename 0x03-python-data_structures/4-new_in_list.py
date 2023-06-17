#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if my_list:

        #create a new list 
        new_list = list.copy(my_list)
        
        if idx < 0 or idx > len(my_list):
            return my_list

        # Add the element into the new list
        new_list[idx] = element
        return new_list
        
