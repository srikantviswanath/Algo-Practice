from trees import is_leaf_node, build_binary_tree


def numberize(digits):
    total = 0
    for i, digit in enumerate(digits[::-1]):
        total += digit * (10 ** i)
    return total


def sum_of_path_numbers(root):
    """
    Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a
    number. Find the total sum of all the numbers represented by all paths.
    """
    total = {'total': 0}  # inner functions of python cannot outer function's variables unless they are mutable

    def helper(root, current_path):
        if not root:
            return
        if is_leaf_node(root):
            total['total'] += numberize(current_path + [root.val])
            return
        helper(root.left, current_path + [root. val])
        helper(root.right, current_path + [root. val])

    helper(root, [])
    return total['total']


if __name__ == '__main__':
    root = build_binary_tree([1, 7, 9, None, None, 2, 9])
    print(sum_of_path_numbers(root))