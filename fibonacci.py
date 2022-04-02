#!/usr/bin/env python3

import re


def get_nth_number(n):
    result = {1: 0, 2: 1, 3: 1}
    if n in result:
        return result[n]

    result[n] = get_nth_number(n-1) + get_nth_number(n-2)
    return result[n]

print(get_nth_number(5))



