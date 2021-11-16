# balanced binary tree 

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def height(root:Node):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1  

def isBalanced(root:Node):
    if root is None:
        return True
    
    left_h = height(root.left)
    right_h = height(root.right)

    # just an upgrade to speedup a little (optional)
    if(left_h == 0 and right_h == 0):
        return True

    if abs(left_h - right_h) <= 1 and isBalanced(root.left) and isBalanced(root.right):
        return True

    return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)

if isBalanced(root):
	print("Tree is balanced")
else:
	print("Tree is not balanced")        