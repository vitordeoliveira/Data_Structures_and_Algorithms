# Max-Heap data structure in Python

class MaxHeap:
    def __init__(self):
        self.arr = []

    def heapify(self, treeNode):
        bigger = treeNode
        left = 2 * treeNode + 1
        rigth = 2 * treeNode + 2

        if(left < len(self.arr) and self.arr[left] > self.arr[bigger]):
            bigger = left

        if(rigth < len(self.arr) and self.arr[rigth] > self.arr[bigger]):
            bigger = rigth

        if(treeNode != bigger):
            self.arr[treeNode], self.arr[bigger] = self.arr[bigger], self.arr[treeNode]
            self.heapify(bigger)

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
        print(f"Max Heap:{str(self.arr)}")

    def delete(self, index):
        self.arr[-1], self.arr[index] =  self.arr[index], self.arr[-1]
        self.arr.pop()
        for index in self.findTrees():
                self.heapify(index)
        


maxheap = MaxHeap()


maxheap.insert(1)
maxheap.insert(2)
maxheap.insert(3)
maxheap.insert(4)
maxheap.insert(5)
maxheap.insert(6)
maxheap.insert(7)

# Peek is the first
maxheap.print()

# Extract is delete the first node
maxheap.delete(0)
maxheap.delete(0)
maxheap.print()
