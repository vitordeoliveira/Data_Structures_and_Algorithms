# Circular Queue implementation in Python


class MyCircularQueue():
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def enqueue(self, value):
        if (self.next_tail_position() == self.head):
            print("Circular queue is full")
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[0] = value
        else:
            self.tail = self.next_tail_position()
            self.queue[self.tail] = value

    def dequeue(self):
        if (self.head == -1):
            print("Circular queue is empty")
        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = self.next_head_position()
            return temp

    def next_tail_position(self):
        return (self.tail + 1) % self.k

    def next_head_position(self):
        return (self.head + 1) % self.k

    # def printCQueue(self):
    #     if(self.head == -1):
    #         print("No element in the circular queue")

    #     elif (self.tail >= self.head):
    #         for i in range(self.head, self.tail + 1):
    #             print(self.queue[i], end=" ")
    #         print()
    #     else:
    #         for i in range(self.head, self.k):
    #             print(self.queue[i], end=" ")
    #         for i in range(0, self.tail + 1):
    #             print(self.queue[i], end=" ")
    #         print()




# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial queue")
# obj.printCQueue()

obj.dequeue()
obj.dequeue()
print("After removing an element from the queue")
# obj.printCQueue()
