#!/usr/bin/env python3


def solve(s):
    # result = s.split()
    # out = []
    # for x in result:
    #     if x.isalpha() and not x[:1].isdigit():
    #         out.append(x.capitalize())
    #     else:
    #         out.append(x)
    # return " ".join(out)
    s = s.split(" ")
    return(" ".join(x.capitalize() for x in s))


s = "monir 1khan"
print(solve(s))
