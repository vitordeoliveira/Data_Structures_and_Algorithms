# Doubly Linked list implementation in Python

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert at the beginning
    def unshift(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

        if (self.head.next == None):
            self.tail = self.head

    # Insert at the end
    def push(self, value):
        new_node = Node(value)

        if (self.tail == None):
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # Insert after a node
    def insertAfter(self, value, position):
        position_node = self.retrieve(position)
        new_node = Node(value)
        new_node.prev = position_node
        new_node.next = position_node.next
        position_node.next.prev = new_node
        position_node.next = new_node

    # Insert before a node
    def insertBefore(self, value, position):
        position_node = self.retrieve(position)
        previous_node = position_node.prev

        if(previous_node == None):
            self.unshift(value)
        else:
            new_node = Node(value)
            previous_node.next = new_node
            new_node.prev = previous_node
            new_node.next = position_node
            position_node.prev = new_node

    # Insert in a especific position
    def insert(self, value, position):
        self.insertBefore(value, position)

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

    # Print LinkedList
    def printListReverse(self):
        tempNode = self.tail
        while (tempNode != None):
            print(tempNode.value, end=" ")
            tempNode = tempNode.prev
        print()


if __name__ == "__main__":
    doublylinkedlist = DoublyLinkedList()

    doublylinkedlist.push(1)
    doublylinkedlist.unshift(2)
    doublylinkedlist.push(3)
    doublylinkedlist.push(4)
    print("Original")
    doublylinkedlist.printList()

    doublylinkedlist.insertAfter(5, 1)
    print("NEW after insert")
    doublylinkedlist.printList()

    doublylinkedlist.insertBefore(10, 1)
    print("NEW before insert")
    doublylinkedlist.printList()

    print("Print reverse list")
    doublylinkedlist.printListReverse()

    # doublylinkedlist.delete(1)
    # print("NEW after delete")
    # doublylinkedlist.printList()
