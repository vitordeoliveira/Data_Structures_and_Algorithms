# Min-Heap data structure in Python

class MinHeap:
    def __init__(self):
        self.arr = []

    def heapify(self, treeNode):
        lowest = treeNode
        left = 2 * treeNode + 1
        rigth = 2 * treeNode + 2

        if(left < len(self.arr) and self.arr[left] < self.arr[lowest]):
            lowest = left

        if(rigth < len(self.arr) and self.arr[rigth] < self.arr[lowest]):
            lowest = rigth

        if(treeNode != lowest):
            self.arr[treeNode], self.arr[lowest] = self.arr[lowest], self.arr[treeNode]
            self.heapify(lowest)

    def insert(self, num):
        size = len(self.arr)
        if(size == 0):
            self.arr.append(num)
        else:
            self.arr.append(num)
            for index in self.findTrees():
                self.heapify(index)

    def findTrees(self):
        return list(range((len(self.arr)//2), -1, -1))

    def print(self):
        print(f"Min Heap:{str(self.arr)}")

    def deleteIndex(self, index):
        self.arr[-1], self.arr[index] =  self.arr[index], self.arr[-1]
        self.arr.pop()
        for index in self.findTrees():
                self.heapify(index)


minheap = MinHeap()
minheap.insert(1)
minheap.insert(2)
minheap.insert(3)
minheap.insert(4)
minheap.insert(5)
minheap.insert(6)
minheap.insert(7)
minheap.insert(-1)
minheap.print()
minheap.deleteIndex(0)
minheap.deleteIndex(0)
minheap.deleteIndex(0)
minheap.print()

