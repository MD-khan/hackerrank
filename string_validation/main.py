#!/usr/bin/env python3

# In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

string = "qA2"

line_1 = any(c.isalnum() for c in string)
print(line_1)

line_2 = any(c.isalpha() for c in string)
print(line_2)

line_3 = any(c.isdigit() for c in string)
print(line_3)

line_4 = any(c.islower() for c in string)
print(line_4)

line_5 = any(c.isupper() for c in string)
print(line_5)


