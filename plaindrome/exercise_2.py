#!/usr/bin/env python3

# queue is FIFO
# stack is LIFO 


strings = "racecar"
queue = []
stack = []

for s in strings:
    queue.append(s)
    stack.append(s)

# dequeue
deque = []
for i in range(len(stack)):
    if stack.pop(i) == queue[i]:
        print("yes")
