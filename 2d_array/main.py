#!/usr/bin/env python3



arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]



# print(arr[0][0:3])
# print(arr[1][1])
# print(arr[2][0:3])

# print()

# print(arr[1][1:4])
# print(arr[2][2])
# print(arr[3][1:4])

# print()

# print(arr[2][2:5])
# print(arr[3][3])
# print(arr[4][2:5])



def cal_hour_glass():
    result = []
    for i in range(0, 4):
        for j in range(0, 4):
            #print(arr[x][y:y+3])
            #add = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            print(f"{arr[i][j:j+3]} {arr[i+1][j+1]} {arr[i+2][j:j+3]}")
            #result.append(add)
    #return max(result)

print(cal_hour_glass())
