#!/usr/bin/python3
import hidden_4 as h

if __name__ == "__main__":
    # Use the dir() function to list all available attributes of the module
    module_attrs = dir(h)
    # Filter out names that don't start with '_'
    filtered_attrs = [attr for attr in module_attrs if not attr.startswith('_')]
    # Print the filtered attributes
    for attr in filtered_attrs:
        print(attr)
