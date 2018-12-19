"""
4.2 Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm
to create a binary search tree with minimal height.
"""
from trees import TreeNode, print_level_order


def minimal_tree(array):
    if not array:
        return
    mid = len(array) // 2
    root = TreeNode(array[mid])
    root.left = minimal_tree(array[:mid])
    root.right = minimal_tree(array[mid+1:])
    return root

if __name__ == '__main__':
    array = [3, 6, 7, 8, 9, 10, 11]
    root = minimal_tree(array)
    print_level_order(root)
