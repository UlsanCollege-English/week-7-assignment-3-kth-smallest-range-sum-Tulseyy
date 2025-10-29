class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    # TODO: return new root after insert (reject duplicates)
    if root is None:
        return Node(key)
    if key == root.key:
        # reject duplicates: do nothing
        return root
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def kth_smallest(root, k):
    # TODO
    if root is None:
        raise IndexError("k is out of bounds")
    if k <= 0:
        raise IndexError("k is out of bounds")

    stack = []
    node = root
    count = 0
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        count += 1
        if count == k:
            return node.key
        node = node.right

    # if we exhaust the tree before reaching k
    raise IndexError("k is out of bounds")

def range_sum_bst(root, low, high):
    # TODO
    if root is None:
        return 0
    total = 0
    # if current node's key is within range, include it and search both sides
    if low <= root.key <= high:
        total += root.key
        total += range_sum_bst(root.left, low, high)
        total += range_sum_bst(root.right, low, high)
    elif root.key < low:
        # current and left subtree too small
        total += range_sum_bst(root.right, low, high)
    else:  # root.key > high
        # current and right subtree too large
        total += range_sum_bst(root.left, low, high)
    return total
