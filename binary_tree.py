class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current


def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root


# function for calculating and returning max value of binary tree
def max_value_binary_tree(root_node):
    current = root_node

    while current.right:
        current = current.right
    return current.val


# function for calculating and returning min value of binary tree (using min_value_node(node) function)
def min_value_binary_tree(root_node):
    return min_value_node(root_node).val


# function for calculating sum of all values in binary tree
def sum_value_binary_tree(root_node):
    if (root_node == None):
        return 0
    
    return (root_node.val + sum_value_binary_tree(root_node.left) +
                       sum_value_binary_tree(root_node.right)) 


# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

root = delete(root, 7)
print(root)

print('Max value of binary tree:', max_value_binary_tree(root), sep='\n')
print('Min value of binary tree:', min_value_binary_tree(root), sep='\n')
print('Sum of all values in binary tree:', sum_value_binary_tree(root), sep='\n')
