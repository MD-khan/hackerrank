#!/usr/bin/env python3


"""
first i is 1 count 1
is second i 1 count 1+1 = 2
is third i 1 no -- continue
add previous count in a dictionery count0 :2
 is fourth i is 1 no -- continue
 is fifith i is 1, yes count1 = 1
"""
import random

def count_ones():
    numbers = decimal_to_binary(13)
    # num_strg = list(map(str, numbers)) # converting int to str
    # num_strg = ''.join(num_strg)
    # num_strg = num_strg.split('0')
    # num_strg = max(num_strg)
    # num_strg = len(num_strg)
    num_strg = max(''.join(list(map(str, numbers))).split('0'))
    return len(num_strg)


    # return onese

result = []
def decimal_to_binary(d):
    if d >= 1:
        decimal_to_binary(d // 2)
        result.append(d % 2) 
        return result

print(count_ones())