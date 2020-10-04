from trees import TreeNode


def find_diameter(root: TreeNode) -> int:
    """Given a binary tree, find the length of its diameter. The diameter of a tree is the number of nodes on the
     longest path between any two leaf nodes. The diameter of a tree may or may not pass through the root."""

    diameter = {'diameter': float('-inf')}

    def diameter_helper(root):
        if not root:
            return 0
        left_ret = diameter_helper(root.left)
        right_ret = diameter_helper(root.right)
        diameter['diameter'] = max(diameter['diameter'], left_ret + right_ret + 1)
        return max(left_ret, right_ret) + 1

    diameter_helper(root)
    return int(diameter['diameter'])


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Tree Diameter: " + str(find_diameter(root)))
    root.left.left = None
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    root.right.left.right.left = TreeNode(10)
    root.right.right.left.left = TreeNode(11)
    print("Tree Diameter: " + str(find_diameter(root)))