# Checking if a binary tree is a complete binary tree in Python


class Node:
    def __init__(self, item) -> None:
        self.item = item
        self.left = None
        self.right = None


def count_nodes(node: Node):
    if(node is None):
        return 0

    return 1 + count_nodes(node.left) + count_nodes(node.right)


def isComplete(root: Node, total_number_of_nodes: int, index: int = 0) -> bool:

    if root is None:
        return True

    if(index >= total_number_of_nodes):
        return False

    return (isComplete(root.left, total_number_of_nodes, (index * 2 + 1))
            and isComplete(root.right, total_number_of_nodes, (index * 2 + 2)))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
# root.right.right = Node(3)
root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)

node_counts = count_nodes(root)

if(isComplete(root, node_counts)):
    print("Is a complete Binary Tree")
else:
    print("Is NOT a complete Binary Tree")
