#!/usr/bin/env python3

# n = int(input())
# arr = map(int, input().split())

list1 = [2, 3, 6, 6, 5]
# create list with removing largest number
sublist = [x for x in list1 if x < max(list1)]

second_larg = max(sublist)
print(second_larg)