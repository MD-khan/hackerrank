#!/usr/bin/env python3

# Main Solution

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 


class Solution:

    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
        #Complete this method
        # if head == None:
        #     return Node(data)
        # head.next = insert(head.next, data)
        print(data, end= ' ')

mylist= Solution()
T=int(input())
head=None

for i in range(T):
    data = int(input())
    head = mylist.insert(head,data)

mylist.display(head)