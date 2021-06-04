# Circular Linked List

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = self
