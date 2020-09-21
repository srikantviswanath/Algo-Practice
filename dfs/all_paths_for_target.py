"""Given a binary tree and a number ‘S’, find all paths from root-to-leaf
such that the sum of all the node values of each path equals ‘S’."""
from trees import build_binary_tree


def is_leaf_node(node):
    return not node.left and not node.right


def find_paths(root, target):
    """
    Space complexity for recursion stack -> O(N)
    Space complexity for all_paths list -> worst case all paths qualify => height * number_of_leaves => logN * N/2 => O(N*logN)
    Time -> O(N)
    """
    all_paths = []

    def helper(root, target, paths):
        if not root:
            return
        if is_leaf_node(root) and target == root.val:
            all_paths.append(paths + [root.val])
            return
        target -= root.val
        helper(root.left, target, paths + [root.val])
        helper(root.right, target, paths + [root.val])
    helper(root, target, [])
    return all_paths


if __name__ == '__main__':
    root = build_binary_tree([12, 7, 1, None, 4, 10, 5])
    print(find_paths(root, 23))
