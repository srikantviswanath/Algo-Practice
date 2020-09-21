from trees import TreeNode, build_binary_tree


def is_leaf_node(node: TreeNode):
    return not node.left and not node.right


def has_path(root: TreeNode, target: int) -> bool:
    """
    Time complexity #
    The time complexity of the above algorithm is O(N)O(N), where ‘N’ is the total number of nodes in the tree.
    This is due to the fact that we traverse each node once.

    Space complexity #
    The space complexity of the above algorithm will be O(N)O(N) in the worst case. This space will be used to
    store the recursion stack. The worst case will happen when the given tree is a linked list
    (i.e., every node has only one child)
    """
    if not root:
        return False
    if is_leaf_node(root) and target == root.val:
        return True
    elif is_leaf_node(root) and target != root.val:
        return False
    target -= root.val
    return has_path(root.left, target) or has_path(root.right, target)


if __name__ == '__main__':
    root = build_binary_tree([12, 7, 1, None, 9, 10, 5])
    print(has_path(root, 16))
    root = build_binary_tree(([1, 2, 3, 4, 5, 6, 7, None, None, None, None, 1, 2, None, None]))
    print(has_path(root, 10))