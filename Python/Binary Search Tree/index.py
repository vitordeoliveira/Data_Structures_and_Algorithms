# Binary Search Tree operations in Python

class Node:
    def __init__(self, value):
        self.value:int = value
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
            current_node.right = self.insert(
                value, current_node.right, counts+1)

        return current_node

    def print_inorder(self, current_node=None, count=0):
        if count == 0:
            current_node = self.root

        if current_node is not None:
            self.print_inorder(current_node.left, count+1)
            print(current_node.value, end="->")
            self.print_inorder(current_node.right, count+1)

    def minValue(self, current_node: Node = None):
        if current_node is not None:
            copy = current_node
        else:
            copy = self.root
        while(copy.left is not None):
            copy = copy.left
        # print(f'\n{copy.value}')
        return copy

    def deleteNode(self, value, current_node: Node = None, count=0):

        if self.root is None:
            return

        if count == 0:
            current_node = self.root

        if current_node is None:
            return current_node

        if value < current_node.value:
            current_node.left = self.deleteNode(
                value, current_node.left, count+1)
        elif value > current_node.value:
            current_node.right = self.deleteNode(
                value, current_node.right, count+1)
        else:
            
            if current_node.left is None:
                temp = current_node.right
                current_node = None
                if count == 0:
                    self.root = temp
                return temp
            elif current_node.right is None:
                temp = current_node.left
                current_node = None
                if count == 0:
                    self.root = temp
                return temp

            temp = self.minValue(current_node.right)

            current_node.value = temp.value

            # Delete the inorder successor
            current_node.right = self.deleteNode(temp.value, current_node.right, count+1)
        
        return current_node


tree = TreeBST()


tree.insert(3)
tree.insert(2)
tree.insert(1)
tree.insert(1)

tree.insert(3.1)

# tree.print_inorder()
# tree.minValue()
# print()

# tree.deleteNode(1)
# tree.print_inorder()
# print()
tree.print_inorder()
print()

tree.deleteNode(3)
tree.deleteNode(2)
tree.deleteNode(1)
tree.deleteNode(3.1)
# tree.deleteNode(3)
# tree.deleteNode(4)
tree.print_inorder()
print()



