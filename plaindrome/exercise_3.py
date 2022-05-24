#!/usr/bin/env python3

my_list = list(range(0,10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#print(my_list)

# add new element at the end
my_list.append(10)

# add element at any given index
my_list.insert(2, 20)

# remove item the last item or top item
my_list.pop()
#print(my_list)

# remove any value
my_list.remove(20)
#print(my_list)

from collections import deque
from random import randrange

linked_list = deque()
linked_list.append(1)
linked_list.append(2)
linked_list.appendleft(0)
linked_list.appendleft(9)

#print(linked_list)

#queueq FIFP
queque = deque()    

for i in range(0,5):
    queque.append(i)
    #print(queque)

for i in range(len(queque)):
    queque.popleft()
    print(queque)


# stack LIFO
stack = deque()





