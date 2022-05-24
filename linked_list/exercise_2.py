#!/usr/bin/env python3

# source https://www.youtube.com/watch?v=Hj_rA0dhr2I

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

def printList(head):
    current = head
    while current != None:
        print(current.data, end=" ")
        current = current.next
    print()



printList(c)