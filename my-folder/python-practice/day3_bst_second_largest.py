class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if not root:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def find_second_largest(root):
    parent = None
    current = root

    while current and current.right:
        parent = current
        current = current.right

    if current.left:
        current = current.left
        while current.right:
            current = current.right
        return current.value

    return parent.value


# Build BST
values = [50, 30, 70, 20, 40, 60, 80]
root = None
for val in values:
    root = insert(root, val)

print("Second Largest Node:", find_second_largest(root))