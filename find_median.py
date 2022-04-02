#!/usr/bin/env python3

def findMedian(arr):
    arr.sort()
    position = int(len(arr) / 2)
    print(arr[position])


arr = [7, 1, 3, 4, 5, 5]
findMedian(arr)
