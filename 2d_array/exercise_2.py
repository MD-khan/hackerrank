#!/usr/bin/env python3

# find the maximum sum in a row

if __name__ == '__main__':

    arr = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]

    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))
    # for element in arr:
    #     print(element)
    # find the maximum sum in a row
    max_sum = 0
    result = 0

    # r1 = arr[0][0]+arr[0][1]+arr[0][2]+arr[0][3]+arr[0][4]+arr[0][5]
    for i in range(6):
        result = arr[i][0]+arr[i][1]+arr[i][2]+arr[i][3]+arr[i][4]+arr[i][5]
        if result >= max_sum:
            max_sum = result

    print(max_sum)
