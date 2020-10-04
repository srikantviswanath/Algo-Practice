from trees import TreeNode


def find_maximum_path_sum(root: TreeNode) -> int:
    max_sum = {'sum': float('-inf')}

    def helper(root):
        if not root:
            return 0

        left_sum, right_sum = helper(root.left), helper(root.right)
        max_sum['sum'] = max(max_sum['sum'], left_sum + right_sum + root.val, root.val)
        return max(left_sum, right_sum) + root.val

    helper(root)
    return int(max_sum['sum'])


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))
    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))