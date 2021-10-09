# Fibonacci Heap in python

import math

# Creating fibonacci tree


class FibonacciTree:
    def __init__(self, value) -> None:
        self.value = value
        self.child = []
        self.order = 0

    def add_at_end(self, t):
        self.child.append(t)
        self.order = self.order + 1

    def __str__(self) -> str:
        return f'value: {self.value} \n order: {self.order} \n child: {self.child} \n'

# Creating Fibonacci heap


class FibonacciHeap:
    def __init__(self) -> None:
        self.trees = []
        self.min = None
        self.count = 0

    def insert_node(self, value) -> None:
        new_tree = FibonacciTree(value)
        self.trees.append(new_tree)
        if(self.min is None or value < self.min.value):
            self.min = new_tree
        self.count = self.count + 1

    def get_min(self):
        if(self.min == None):
            print('None')
        else:
            print(self.min.value)

    def extract_min(self):
        smallest = self.min
        if smallest is not None:
            for child in smallest.child:
                self.trees.append(child)
            self.trees.remove(smallest)
            if self.trees == []:
                self.min = None
            else:
                self.min = self.trees[0]
                self.consolidate()
                self.count = self.count - 1
            print(f"{smallest.value} removed!")

    def consolidate(self):
        # Store the new consolidate nodes
        aux = floor_log(self.count) * [None]

        while self.trees != []:
            x = self.trees[0]
            order = x.order
            self.trees.remove(x)
            while aux[order] is not None:
                y = aux[order]
                if x.value > y.value:
                    x, y = y, x
                x.add_at_end(y)
                aux[order] = None
                order = order + 1
            aux[order] = x

        # Is a filter to add just the non empty aux nodes
        self.min = None
        for k in aux:
            if k is not None:
                self.trees.append(k)
                if(self.min is None or k.value < self.min.value):
                    self.min = k


def floor_log(x):
    return math.floor((math.log(x) * 2))

fibonacci_heap = FibonacciHeap()

fibonacci_heap.insert_node(-1)
fibonacci_heap.insert_node(1)
fibonacci_heap.insert_node(2)
fibonacci_heap.insert_node(3)
fibonacci_heap.insert_node(4)
fibonacci_heap.insert_node(5)

fibonacci_heap.extract_min()




