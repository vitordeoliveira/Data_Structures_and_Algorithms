# AVL tree implementation in Python
import sys


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None
        self.height = 1


class AVLTree:
    def insert_node(self, root: Node, value) -> Node:

        # Find the correct location and insert the node
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self.insert_node(root.left, value)
        else:
            root.right = self.insert_node(root.right, value)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)

        if balanceFactor > 1:
            if value <= root.left.value:
                return self.rigthRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rigthRotate(root)

        if balanceFactor < -1:
            if value >= root.right.value:
                return self.leftRotate(root)
            else:
                root.right = self.rigthRotate(root.right)
                return self.leftRotate(root)

        return root

    def leftRotate(self, z: Node) -> None:
        y: Node = z.right
        T2 = y.left
        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    def rigthRotate(self, z: Node) -> None:
        y: Node = z.left
        T2 = y.right
        y.right = z
        z.left = T2

        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    def getBalance(self, root: Node) -> int:
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getHeight(self, root: Node) -> int:
        if not root:
            return 0
        return root.height

    def getMinValueNode(self, root) -> None:
        node = root
        while(node is not None and node.left is not None):
            node = node.left
        return node

    def delete_node(self, root: Node, value) -> Node:

        if root is None:
            return root

        if value < root.value:
            root.left = self.delete_node(root.left, value)
        elif value > root.value:
            root.right = self.delete_node(root.right, value)
        else:

            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getMinValueNode(root.right)
            root.value = temp.value
            root.right = self.delete_node(root.right, temp.value)


        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rigthRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rigthRotate(root)

        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rigthRotate(root.right)
                return self.leftRotate(root)

        return root

    def print_inorder(self, current_node=None, count=0):
        # if count == 0:
        #     current_node = self.root

        if current_node is not None:
            self.print_inorder(current_node.left, count+1)
            print(current_node.value, end="->")
            self.print_inorder(current_node.right, count+1)

    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.value)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)


tree = AVLTree()
root = None


root = tree.insert_node(root, 6)
root = tree.insert_node(root, 213)

nums = [6,1,3,10,5,213]
for num in nums:
    root = tree.insert_node(root, num)
    # root = tree.delete_node(root, num)

root = tree.delete_node(root, 213)
root = tree.delete_node(root, 213)
root = tree.delete_node(root, 6)
root = tree.delete_node(root, 6)

tree.printHelper(root, "", True)
# print(tree.getMinValueNode(root))
