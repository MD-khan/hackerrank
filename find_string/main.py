#!/usr/bin/env python3

#  In this challenge, the user enters a string and a substring.
#  You have to print the number of times that the substring occurs in the given string.
#  String traversal will take place from left to right, not from right to left.
# Input     ABCDCDC
# substring CDC
# Out put 2

# string = input().strip()
# sub_string = input().strip()

string = "ABCDCDC"
sub_string = "CDC"

def count_substring(string, sub_string):
    count = 0
    for index in range(len(string)):
        if string.startswith(sub_string, index):
            count = count + 1
    return count


count_substring(string, sub_string)