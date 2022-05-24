#!/usr/bin/env python3

""""
10 2 8
10 -2 = 8
10 - 8 = 2
2- 10 = - 8
2 - 8  = -6
"""

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

	# Add your code here
    def computeDifference(self):
        l = []
        for i in range(len(self.__elements)-1):
            for j in range(len(self.__elements)-1):
                #print(self.__elements[i] - self.__elements[j+1])
                s = self.__elements[i] - self.__elements[j+1]
                l.append(abs(s))
        self.maximumDifference = max(l)


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

""""
3    
1 2 5
"""