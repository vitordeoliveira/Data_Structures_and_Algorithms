# Circular Linked List

class Node:
    def __init__(self, data=None):
        self.value = data
        self.next = self

class CircularLL:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, value) -> None:
        new_node = Node(value)
        if(self.count == 0 ):
            self.count = self.count + 1
            self.head = new_node
            self.tail = new_node
        else:  
            self.count = self.count + 1
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        print(self)

    def __str__(self) -> str:
        string = "Circular Linked List"
        if(self.head == None):
            string += " Empty"
            return string
        
        string += f": \n{self.head.value}"

        temp_node = self.head.next

        while(temp_node != self.head):
            string += f" -> {temp_node.value}"
            temp_node = temp_node.next
        
        string += f'-> and the next one is {temp_node.value}'

        return string



CLL = CircularLL()

CLL.append(1)
CLL.append(2)
CLL.append(3)
CLL.append(4)

CLL.display()
        
