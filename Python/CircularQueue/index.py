# Circular Queue implementation in Python


class MyCircularQueue():
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def enqueue(self, value):
        # print("Enqueue, value:", value)
        if (self.next_tail_position() == self.head):
            print(f"Circular queue is full, value: {value} is not added")
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[0] = value
            self.printCQueue()
        else:
            self.tail = self.next_tail_position()
            self.queue[self.tail] = value
            self.printCQueue()
        

    def dequeue(self):
        if (self.head == -1):
            print("Circular queue is empty")
        elif (self.head == self.tail):
            self.head = -1
            self.tail = -1
        else:
            self.head = self.next_head_position()

        self.printCQueue()
        

    def next_tail_position(self):
        return (self.tail + 1) % self.k

    def next_head_position(self):
        return (self.head + 1) % self.k

    def printCQueue(self):
        if(self.head == -1):
            print("No elemenst on circular queue")
        elif (self.tail >= self.head):
            for i in range(self.head, self.tail+ 1):
                print(self.queue[i], end=" ")
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
        
        print()



# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
obj.enqueue(6)

obj.dequeue()
obj.dequeue()
obj.dequeue()

obj.enqueue(6)
obj.enqueue(7)
obj.enqueue(8)
obj.enqueue(9)

obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.dequeue()



