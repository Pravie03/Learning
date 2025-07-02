class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_valid_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        return True

    if not (min_val < node.value < max_val):
        return False

    return (is_valid_bst(node.left, min_val, node.value) and
            is_valid_bst(node.right, node.value, max_val))

# Build valid BST
root = Node(10)
root.left = Node(5)
root.right = Node(15)

# Add invalid data (uncomment to test failure)
# root.right.left = Node(9)  # violates BST rule

print("Is valid BST?", is_valid_bst(root))