# 1. Implement Binary tree.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    else:
        if value < root.value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
        return root

def search(root, value):
    if root is None or root.value == value:
        return root
    if value < root.value:
        return search(root.left, value)
    return search(root.right, value)

def inorder_traversal(root):
    result = []
    if root:
        result = inorder_traversal(root.left)
        result.append(root.value)
        result += inorder_traversal(root.right)
    return result

root = None
values = [5, 3, 8, 2, 4, 7, 9]

for value in values:
    root = insert(root, value)

print("Inorder Traversal:", inorder_traversal(root))

target_value = 4
result = search(root, target_value)
if result:
    print(f"Value {target_value} found in the binary tree.")
else:
    print(f"Value {target_value} not found in the binary tree.")

# 2. Find height of a given tree.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_height(root):
    if root is None:
        return -1

    left_subtree_height = tree_height(root.left)
    right_subtree_height = tree_height(root.right)

    return max(left_subtree_height, right_subtree_height) + 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

height = tree_height(root)
print("Height of the tree:", height)

# 3. Perform Pre-order, Post-order, In-order traversal.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_traversal(node):
    if node is not None:
        print(node.value, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.value, end=" ")
        inorder_traversal(node.right)

def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value, end=" ")

# Construct the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# Pre-order traversal
print("Pre-order Traversal:")
preorder_traversal(root)
print()

# In-order traversal
print("In-order Traversal:")
inorder_traversal(root)
print()

# Post-order traversal
print("Post-order Traversal:")
postorder_traversal(root)
print()

# 4. Function to print all the leaves in a given binary tree.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_leaves(root):
    if root is not None:
        if root.left is None and root.right is None:
            print(root.value)
        else:
            print_leaves(root.left)
            print_leaves(root.right)

# Construct the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print("Leaves of the binary tree:")
print_leaves(root)

# 5. Implement BFS (Breath First Search) and DFS (Depth First Search).

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs(root):
    if root is None:
        return

    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.value, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def dfs_preorder(root):
    if root is None:
        return

    print(root.value, end=" ")
    dfs_preorder(root.left)
    dfs_preorder(root.right)

def dfs_inorder(root):
    if root is None:
        return

    dfs_inorder(root.left)
    print(root.value, end=" ")
    dfs_inorder(root.right)

def dfs_postorder(root):
    if root is None:
        return

    dfs_postorder(root.left)
    dfs_postorder(root.right)
    print(root.value, end=" ")

# Construct the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print("Breadth-First Search (BFS):")
bfs(root)
print("\nDepth-First Search (DFS) - Preorder:")
dfs_preorder(root)
print("\nDepth-First Search (DFS) - Inorder:")
dfs_inorder(root)
print("\nDepth-First Search (DFS) - Postorder:")
dfs_postorder(root)

# 6. Find sum of all left leaves in a given Binary Tree.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sum_of_left_leaves(root):
    if root is None:
        return 0

    if root.left and root.left.left is None and root.left.right is None:
        left_leaf_sum = root.left.value
    else:
        left_leaf_sum = 0

    return left_leaf_sum + sum_of_left_leaves(root.left) + sum_of_left_leaves(root.right)

# Construct the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print("Sum of left leaves in the binary tree:", sum_of_left_leaves(root))

# 7. Find sum of all nodes of the given perfect binary tree.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sum_of_nodes(root):
    if root is None:
        return 0

    return root.val + sum_of_nodes(root.left) + sum_of_nodes(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

total_sum = sum_of_nodes(root)
print("Sum of all nodes:", total_sum)

# 8. Count sub tress that sum up to a given value x in a binary tree.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def count_subtrees_with_sum(root, target_sum):
    def count_subtrees_with_sum_helper(node, target_sum):
        if not node:
            return 0, 0

        left_sum, left_count = count_subtrees_with_sum_helper(node.left, target_sum)
        right_sum, right_count = count_subtrees_with_sum_helper(node.right, target_sum)

        total_sum = left_sum + right_sum + node.val
        total_count = left_count + right_count

        if total_sum == target_sum:
            total_count += 1

        return total_sum, total_count

    _, count = count_subtrees_with_sum_helper(root, target_sum)
    return count

# Creating a binary tree
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(11)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)

target_sum = 8
count = count_subtrees_with_sum(root, target_sum)
print("Number of subtrees with sum {} is: {}".format(target_sum, count))

# 9. Find maximum level sum in Binary Tree.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_level_sum(root):
    if not root:
        return 0

    max_sum = float('-inf')
    queue = [root]

    while queue:
        level_sum = 0
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.pop(0)
            level_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        max_sum = max(max_sum, level_sum)

    return max_sum

# Creating a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(8)
root.left.left.left = TreeNode(6)
root.right.right.left = TreeNode(7)
root.right.right.right = TreeNode(9)

max_sum = max_level_sum(root)
print("Maximum level sum:", max_sum)

# 10. Print the nodes at odd levels of a tree.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def print_nodes_at_odd_levels(root):
    def dfs(node, level):
        if not node:
            return

        if level % 2 != 0:
            print(node.val)

        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 1)

# Creating a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(8)
root.left.left.left = TreeNode(6)
root.right.right.left = TreeNode(7)
root.right.right.right = TreeNode(9)

print("Nodes at odd levels:")
print_nodes_at_odd_levels(root)