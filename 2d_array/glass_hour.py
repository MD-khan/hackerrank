#!/usr/bin/env python3

# Create a glass house
#Input : rows = 7
# Output: 
"""
1 2 3 4 5 6 7
 2 3 4 5 6 7
  3 4 5 6 7
   4 5 6 7
    5 6 7
     6 7 
      7
     6 7
    5 6 7
   4 5 6 7
  3 4 5 6 7
 2 3 4 5 6 7
1 2 3 4 5 6 7
"""

def glass_hours(rows):
    #for loop for printing the upper half
    for i in range(1, rows + 1):
        for k in range(1, i):
            print(" ", end="")
        # printing i to rowa value 
        # at the end of each row
        for j in range(i, rows +1):
            print(j, end=" ")
        print()
    # for loop for printing the lower half
    for i in range(rows-1, 0, -1):
        for k in range(1, i):
            print(" ", end="")
        for j in range(i, rows + 1):
            print(j, end=' ')
        print()
        


glass_hours(7)

  
