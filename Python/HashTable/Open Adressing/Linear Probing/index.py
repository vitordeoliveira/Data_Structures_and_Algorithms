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
        self.size = size
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

        # If position of table is empty
        if(self.table[self.position(key)] == 0):
            self.table[self.position(key)] = new_node
            self.elementCount += 1
        elif(self.table[self.position(key)].key == key):
            print(f"Update value of key: {key}1")
            self.table[self.position(key)] = new_node

        # If already have a value on the position
        else:
            # The same thing as DO_WHILE but in python
            while(True):
                print(
                    f"key: {key} with hash of {self.position(key)} colission {colission_counter+1} times")
                colission_counter += 1
                new_position = self.position(key)+colission_counter

                if(new_position >= self.size):
                    new_position -= self.size

                if(colission_counter == self.size):
                    print("Table is Full")
                    break

                if(self.table[new_position] == 0):
                    self.table[new_position] = new_node
                    self.elementCount += 1
                    break
                # If the key already exist and the value is new, update just the value not fill the hash table
                elif(self.table[new_position].key == key):
                    print(f"Update value of key: {key}2")
                    self.table[new_position] = new_node
                    break

    def remove(self, key) -> None:
        while(True):
            if(self.table[self.position(key)] != 0 and self.table[self.position(key)].key == key):
                self.table[self.position(key)] = None
                break

    # method to display the hash table
    def __str__(self):
        string = ""
        for index, i in enumerate(self.table):
            if(i != 0):
                string += (f"{index} - [{i.key}] : {i.value}\n")
            else:
                string += (f"{index} - [{i}]\n")
        return string

    def __getitem__(self, key):
        new_position = self.position(key)
        colission_counter = 0
        while(True):
            print(colission_counter)
            if(colission_counter == self.size):
                print("not found")
                return None

            if(new_position + colission_counter >= self.size):
                new_position -= self.size

            new_position += colission_counter
            if(self.table[new_position] == 0):
                return None
            elif(self.table[new_position].key == key):
                return self.table[new_position].value
            else:
                colission_counter += 1


# main function
hashT = hashTable(8)

hashT.insert(8, "110")
hashT.insert(9, "110")
hashT.insert("developer", [1, 2, 3, 4, 5])
hashT.insert(9, "another string")
hashT.insert("full-Stack", (1, 2, 3, 5))

print(hashT["full-Stack"])
print(hashT)
