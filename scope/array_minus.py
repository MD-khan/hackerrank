#!/usr/bin/env python3
# find the maximum difference between two elements



nums = [1, 2, 5]
# [5, 2, 1]
#nums.sort(reverse=True)
print('List in Ascending Order: ', nums)
l = []
for i in range(len(nums)-1):
    for j in range(len(nums)-1):
        #print(nums[i] - nums[j+1])
        s = nums[i] - nums[j+1]
        l.append(abs(s))
print(max(l))






