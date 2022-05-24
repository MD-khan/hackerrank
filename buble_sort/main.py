#!/usr/bin/env python3

#  bubble sort
#arr = [4,3,1,2]

# arr = [3, 1, 2, 4]
def swap(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)-1):
            if arr[i] > arr[j+1]:
                count += 1
                a = arr[j]
                b  = arr[j+1]
                arr[j] = b
                arr[j+1] = a
            print(arr)
    if arr[0] > arr[1]:
        count += 1
        swap(arr)
    return arr, count

arr = [1, 2, 4]        
result, count = swap(arr)      
print(f"Array is sorted in {count} swaps.")
print(f"First Element: {arr[0]}")
print(f"Last Element: {arr[-1]}")




# def swap(val1, val2):
#     tmp1 = 0
#     tmp2 = 0
#     if val1 > val2:
#         a = val1
#         b  = val2
#         tmp1 = b
#         tmp2 = a
#         return tmp1, tmp2
#     else:
#         return val1, val2
# print(swap(1, 2))



# arr [3, 4, 1, 2] - no
# arr [3, 1, 4, 2]
# compare first two elements
# if first element is larger than second, swap
# otherwise go next twi

# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] > arr[j]:
#             a = arr[i]
#             b = arr[j]
#             arr[j] = b
#             arr[j+1] = a
# print(arr)
