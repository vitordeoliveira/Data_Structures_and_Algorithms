# Deque implementaion in python


class Deque:
    def __init__(self):
        self.queue = []

    def addFront(self, item):
        self.queue.insert(0, item)
        self.print()

    def addNear(self, item):
        self.queue.append(item)
        self.print()


    def removeFront(self):
        self.queue = self.queue[1:]
        self.print()

    def removeNear(self):
        self.queue = self.queue[:-1]
        self.print()
    
    # def removeFront(self):
    #     return self.items.pop(0)

    # def removeRear(self):
    #     return self.items.pop()


    def print(self):
        print(self.queue)

deque = Deque()

deque.addFront(1)
deque.addFront(2)
deque.addFront(3)

deque.addNear(3)
deque.addNear(2)
deque.addNear(1)

deque.removeNear()
deque.removeNear()
deque.removeNear()

deque.removeFront()
deque.addNear(1)
deque.removeNear()
