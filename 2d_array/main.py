#!/usr/bin/env python3

if __name__ == '__main__':

# Sum each row and find the max sum
    arr = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1]
    ]

    arr_r = list(map(sum, arr))
    print(max(arr_r))
