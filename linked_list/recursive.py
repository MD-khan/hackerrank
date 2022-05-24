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

def print_link_list(head):
    if head == None:
        return
    print(head.data, end=" ")
    print_link_list(head.next)

print_link_list(b)