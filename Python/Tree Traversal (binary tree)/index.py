# Tree traversal in Python


class Node:
    def __init__(self,item) -> None:
        self.val = item
        self.r = None
        self.l = None


def preorder(root:Node):
    if root:
        print((root.val), end="-")
        preorder(root.l)
        preorder(root.r)


def inorder(root:Node):
    if root:
        inorder(root.l)
        print((root.val), end="-")
        inorder(root.r)

def postorder(root:Node):
    if root:
        postorder(root.l)
        postorder(root.r)
        print((root.val), end="-")


root = Node(1)
root.l = Node(2)
root.r = Node(3)
root.l.l = Node(4)
root.l.r = Node(5)

print("Inorder traversal ")
inorder(root)

print("\nPreorder traversal ")
preorder(root)

print("\nPostorder traversal ")
postorder(root)
