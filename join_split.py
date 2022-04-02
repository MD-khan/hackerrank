# def split_and_join(line):
#     # write your code here
#     line = line.split(" ")
#     line = "-".join(line)
#     return line

# import re
# import textwrap
# def wrap(string, max_width):
#     result = textwrap.wrap(string, max_width)
#     result = "\n".join(result)
#     return f"{result}" 

# print(wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4))

t = "1chris alan"
re = t.split(" ")
t = [x.capitalize() for x in re if not x[:1].isdigit()]

print(t)
