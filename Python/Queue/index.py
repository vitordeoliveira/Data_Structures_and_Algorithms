# Queue implementation in Python

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def size(self):
        return len(self.queue)

    def dequeue(self):
        if self.size() < 1:
            return None
        self.queue.pop(0)

    def __str__(self):
        return f"{self.queue}"
    
    
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q)

q.dequeue()
print("After removing an element")
print(q)

q.dequeue()
print("After removing an element")
print(q)

q.dequeue()
print("After removing an element")
print(q)
