#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000000)
def factorial(n):
    # 5! = 5*4*3*2*1 
    #   = 120
    return n * factorial(n-1) if n > 1 else 1

print(factorial(20965)) # this is tha max num this pc can calculate
#print(sys.maxsize)

#print(sys.getrecursionlimit())