#!/usr/bin/env python3

s = "Racecar".lower()
if s == s[::-1]:
    print(f"{s} is a plaindrome")
else:
    print(f"{s} is not a plaindrome")
