# Program to implement Hashing with Linear Probing

from typing import Any, Union


class Node:
    def __init__(self, key: Union[str, int], data=None):
        self.key = key
        self.value = data


class hashTable:
    # initialize hash Table

    def __init__(self, size: int) -> None:
        self.table = [0]*size
        self.elementCount = 0
        # list(0 for _ in range(size))

    # method that checks if the hash table is full or not
    def isFull(self) -> bool:
        return self.elementSize == self.size

    # method that returns position for a given element
    def hashFunction(self, element: int) -> None:
        return element % len(self.table)

    # calculate position
    def position(self, key: Union[str, int]) -> int:
        if(isinstance(key, str)):
            sumOfASCII = sum([ord(c) for c in key])
            return self.hashFunction(sumOfASCII)
        if(isinstance(key, int)):
            return self.hashFunction(key)

    # method that inserts element inside the hash table
    def insert(self, key: Union[str, int], value: Any) -> None:
        new_node = Node(key, value)
        colission_counter: int = 0

        if(self.table[self.position(key)] == 0):
            self.table[self.position(key)] = new_node
            self.elementCount += 1
        else:
            while(True):
                print("colission")
                colission_counter += 1
                if(self.table[self.position(key)+colission_counter] == 0):
                    self.table[self.position(key)+colission_counter] = new_node
                    self.elementCount += 1
                    break


    def remove(self, element):
        pass

    # method to display the hash table
    def __str__(self):
        string = ""
        for i in self.table:
            if(i != 0):
                string += (f"[{i.key}] : {i.value}\n")
            else:
                string += (f"[{i}]\n")
        return string


# main function
table1 = hashTable(10)
table1.insert(4, 110)
table1.insert("vitor", 10)
table1.insert("vitor", 10)
table1.insert("vitor", 10)
table1.insert("vitor", 10)
table1.insert("vitor", 10)

print(table1)
