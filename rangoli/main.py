#!/usr/bin/env python3

# Task
# Print an alphabet ragoli of given size

# INPUT 3
# OUTPUT
"""
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
"""
# TODO
# Get the alphabet based on the given size
# -c
# Set alphabet a in the midle
# count the alphabet is left from a


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def rangoli(size):
    if size > 27 or size < 0:
        return
    #line = list(map(chr,range(97,123)))
    midle_row = alphabet[size-1::-1] + alphabet[1:size]
    # add - between chr and get the lenght
    lenght = len("-".join(midle_row))
    for i in range (1, size):
        print("-".join(alphabet[size-1:size-i:-1] + alphabet[size-i:size]).center(lenght,'-'))

    for i in range (size, 0, -1):
        print("-".join(alphabet[size-1:size-i:-1] + alphabet[size-i:size]).center(lenght,'-'))

rangoli(26)


