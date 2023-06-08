#!/usr/bin/python3

# This program prints all the alphabetsexcept q and e

for i in range(97, 123):
    if chr(i) != 'e' and chr(i) != 'q':
        print("{}".format(chr(i)), end="")
