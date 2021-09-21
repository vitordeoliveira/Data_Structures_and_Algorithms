# Max-Heap data structure in Python


class MaxHeap:
    def __init__(self):
        self.arr = []

    def heapify(self, size, index):
        largest = index
        l = 2 * index + 1
        r = 2 * index + 2

        if l < size and self.arr[index] < self.arr[l]:
            largest = l

        if r < size and self.arr[largest] < self.arr[r]:
            largest = r

        if largest != index:
            self.arr[largest], self.arr[index] = self.arr[index], self.arr[largest]
            self.heapify(size, largest)

    def insert():
        pass

    def delete():
        pass


maxheap = MaxHeap()