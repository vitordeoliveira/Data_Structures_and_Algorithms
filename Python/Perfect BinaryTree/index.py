# Checking if a binary tree is a perfect binary tree in Python


class Node:
    def __init__(self, item) -> None:
        self.item = item
        # self.left = None
        # self.right = None
        self.right = self.left = None


def calculateDepth(root: Node):
    d = 0
    while(root.left is not None):
        d += 1
        root = root.left
    return d

# Check if the tree is perfect binary tree


def is_perfect(tree: Node, depth: int, level: int = 0) -> bool:

    if(tree.left is None and tree.right is None):
        return (depth == level)

    if(tree.left is None or tree.right is None):
        return False

    return (is_perfect(tree.right, depth, level + 1) and is_perfect(tree.left, depth, level + 1))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(4)
root.right.right = Node(5)

if (is_perfect(root, calculateDepth(root))):
    print("The tree is a perfect binary tree")
else:
    print("The tree is not a perfect binary tree")
