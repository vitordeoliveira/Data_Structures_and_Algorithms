# Binary Search Tree operations in Python

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TreeBST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value, current_node: Node = None, counts=0):

        if self.root is None:
            self.root = Node(value)
            return None

        if counts == 0:
            current_node = self.root

        if current_node is None:
            return Node(value)

        if current_node.value > value:
            current_node.left = self.insert(value, current_node.left, counts+1)
        else:
            current_node.right = self.insert(value, current_node.right, counts+1)

        return current_node

    def print_inorder(self, current_node=None, count=0):
        if count == 0:
            current_node = self.root

        if current_node is not None:
            self.print_inorder(current_node.left, count+1)
            print(current_node.value, end="-")
            self.print_inorder(current_node.right, count+1)



tree = TreeBST()


tree.insert(3)
tree.insert(2)
tree.insert(1)
tree.insert(1)
tree.insert(2)
tree.insert(1)


tree.print_inorder()
