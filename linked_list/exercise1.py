#!/usr/bin/env python3

class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None


class Linked:
    def __init__(self):
        self.head = None

    def show(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
    
    # add element to the link list at the begining
    def add(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node


link = Linked()
elem = Node('Monir')
link.head = elem

elem2 = Node("Juma")
link.head.next = elem2


# add element at the befgining
link.add('Munisa')
link.add('Musa')

link.show()