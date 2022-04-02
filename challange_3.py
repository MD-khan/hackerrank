#!/usr/bin/env python3

from ntpath import join


if __name__ == '__main__':
    # n = int(input())
    n = 5
    value = []
    for i in range(1, n+1):
        value.append(i)
    value = ''.join(map(str, value))
    print(value)
