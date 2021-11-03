# Checking if a binary tree is a full binary tree in Python


class Node:
    def __init__(self, item) -> None:
        self.item = item
        self.left = None
        self.rigth = None

def isFullBinaryTree(root: Node) -> bool:

    if(root is None):
        return True

    if(root.left is None and root.rigth is None):
        return True

    if(root.left is not None and root.rigth is not None):
        return isFullBinaryTree(root.left) and isFullBinaryTree(root.rigth)

    return False


tree = Node(1)
tree.left = Node(2)
tree.rigth = Node(3)
tree.rigth.rigth = Node(3)


if isFullBinaryTree(tree):
    print("Is a full binary tree")
else:
    print("Is NOT a full binary tree")
