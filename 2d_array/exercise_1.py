#!/usr/bin/env python3

# # 
# n = 5
# arr = [0]*n
# #print(arr)
# #arr = [0 for i in range(n)]


# # 2-dimentional array
# rows, cols = (5,5)
# arr = [[0]*cols] * rows
# #print(arr)

# # lets change the first elemnet of the row 
# arr[0][0] = 1 # this will change the element of each row, because all pointing the same object

# for row in arr:
#     print(row)

# right way to declare 2-dimantional array
rows, cols = (5,5)
arr = [[0 for i in range(cols)] for j in range(rows)]
arr[0][0] = 2
for row in arr:
    print(row)
