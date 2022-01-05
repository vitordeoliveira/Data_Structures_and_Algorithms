# Searching a key on a B-tree in Python
import math

# Create a node


class Node:
    def __init__(self, values=[], child=[], splited=False):
        self.values = values
        self.child = child
        self.splited = splited


# Tree
class BTree:
    def __init__(self, max_children):
        # self.root = Node()
        # Max of child nodes (m)
        self.max_children = max_children
        # Max number of elements in child array
        self.max_elements = max_children-1
        # min number of child nodes
        # self.min_of_child_elements = math.ceil(max_children/2)
        # The child nodes > values
        # All leaf nodes are in the same level

        # Insert node
    def insert(self, current_node: Node, value):
        if current_node is None:
            new_node = Node([value])
            return new_node

        current_node.values.append(value)
        current_node.values.sort()

        if(self.is_leaf(current_node)):
            if(len(current_node.values) > self.max_elements):
                return self.split_child(current_node)
            else:
                return current_node
        else:
            index = current_node.values.index(value)
            current_node.values.pop(index)
            temp = self.insert(current_node.child[index], value)

            # CHECK IF TEMP IS A SPLITED CHILD
            if(temp.splited):
                temp.splited = False
                current_node.child.pop(index)
                current_node.values.append(temp.values[0])
                current_node.child.extend(temp.child)

            if(len(current_node.values) > self.max_elements):
                return self.split_child(current_node)

            return current_node

    def split_child(self, current_node):
        split_element_index = math.floor(len(current_node.values)/2)
        if(self.max_children % 2 == 0):
            split_element_index = split_element_index - 1
        temp = current_node.values[split_element_index]
        current_node.values.pop(split_element_index)
        leftValues = Node(
            current_node.values[:split_element_index], current_node.child[:split_element_index+1])
        rightValues = Node(
            current_node.values[split_element_index:], current_node.child[split_element_index+1:])

        splitedElement = Node(values=[temp], child=[
                              leftValues, rightValues], splited=True)
        return splitedElement

    def is_leaf(self, current_node: Node):
        return len(current_node.child) == 0

    def delete_node(self, current_node, value):
        pass

    # Print the tree
    def print_tree(self, current_node: Node):
        i = 0
        for x in range(len(current_node.values)):
            i += 1
            if(not self.is_leaf(current_node)):
                self.print_tree(current_node.child[x])
            print(current_node.values[x])

        if(not self.is_leaf(current_node)):
            self.print_tree(current_node.child[i])

    # Search key in the tree

    def search_key(self, k, x=None):
        pass


B = BTree(3)
root = None
root = B.insert(root, 1)
root = B.insert(root, 2)
root = B.insert(root, 3)
root = B.insert(root, 4)
root = B.insert(root, 5)
root = B.insert(root, 6)
root = B.insert(root, 7)
root = B.insert(root, 8)
# root = B.insert(root, 9)
# root = B.insert(root, 10)
# root = B.insert(root, 11)
# root = B.insert(root, 12)
# root = B.insert(root, 13)
# root = B.insert(root, 14)
# root = B.insert(root, 15)
# root = B.insert(root, 19)

B.print_tree(root)

# for i in range(10):
#     B.insert((1, 2 * i))

# B.print_tree(B.root)

# if B.search_key(1) is not None:
#     print("\nFound")
# else:
#     print("\nNot Found")
