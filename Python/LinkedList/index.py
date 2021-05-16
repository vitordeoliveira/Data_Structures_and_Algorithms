# Linked list implementation in Python


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert at the beginning
    def unshift(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

        if (self.head.next == None):
            self.tail = self.head

    # Insert at the end
    def push(self, value):
        if (self.tail == None):
            self.head = Node(value)
            self.tail = self.head
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node

    # Insert after a node
    def insertAfter(self, value, position):
        position_node = self.retrieve(position)
        new_node = Node(value)
        new_node.next = position_node.next
        position_node.next = new_node

    # Insert in a especific position
    def insert(self, value, position):
        new_node = Node(value)
        if (position - 1 == -1):
            new_node.next = self.head.next
            self.head = new_node
        else:
            before_node = self.retrieve(position - 1)
            new_node.next = before_node.next.next
            before_node.next = new_node

    # Deleting a node
    def delete(self, position):
        if (position - 1 == -1):
            self.head = self.head.next
        else:
            before_node = self.retrieve(position - 1)
            before_node.next = before_node.next.next

    # Get Node in Position
    def retrieve(self, position):
        if (position == 0):
            return self.head

        temp_node = self.head
        for _ in range(position):
            if (temp_node != None):
                temp_node = temp_node.next

        if (temp_node != None):
            return temp_node

    # Print LinkedList
    def printList(self):
        tempNode = self.head
        while (tempNode != None):
            print(tempNode.value, end=" ")
            tempNode = tempNode.next
        print()

if __name__ == "__main__":
    linkedlist = LinkedList()

    linkedlist.push(1)
    linkedlist.unshift(2)
    linkedlist.push(3)
    linkedlist.push(4)
    print("Original")
    linkedlist.printList()

    linkedlist.insert(5, 3)
    print("NEW after insert")
    linkedlist.printList()

    linkedlist.delete(1)
    print("NEW after delete")
    linkedlist.printList()
