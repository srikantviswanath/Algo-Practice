from trees import print_level_order, build_binary_tree


def diameter(root):
    if not root:
        return 0

    def helper(node):
        if not node:
            return -1, -1
        ll, lr = helper(node.left)
        rl, rr = helper(node.right)
        return 1 + max(ll, lr), 1 + max(rl, rr)

    left_path, right_path = helper(root)
    return left_path + right_path + 1


if __name__ == '__main__':
    root = build_binary_tree([1, 2, 3, 4, 5, None, None, None, 9])
    print(diameter(root))
    print_level_order(root)