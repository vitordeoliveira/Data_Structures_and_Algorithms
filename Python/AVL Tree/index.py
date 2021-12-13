# AVL tree implementation in Python


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None
        self.height = 1


class AVLTree:
    def insert(self, root: Node, value) -> Node:

        # Find the correct location and insert the node
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)

        if balanceFactor > 1:
            if value < root.left.value:
                return self.rigthRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rigthRotate(root)

        if balanceFactor < -1:
            if value > root.right.value:
                return self.leftRotate(root)
            else:
                root.right = self.rigthRotate(root.right)
                return self.leftRotate(root)

        return root

    def leftRotate(self, z: Node) -> None:
        print("leftRotate")
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
        print("rigthRotate")
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

    def getMinValueNode() -> None:
        pass

    def delete() -> None:
        pass

    def print_inorder(self, current_node=None, count=0):
        # if count == 0:
        #     current_node = self.root

        if current_node is not None:
            self.print_inorder(current_node.left, count+1)
            print(current_node.value, end="->")
            self.print_inorder(current_node.right, count+1)


tree = AVLTree()
root = None

root = tree.insert(root, 1)
root = tree.insert(root, 2)
root = tree.insert(root, 1)
# root = tree.insert(root, 9)
# root = tree.insert(root, 213)
# root = tree.insert(root, 321)



tree.print_inorder(root)

