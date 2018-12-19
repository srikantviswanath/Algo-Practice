"""
Given a binary tree, print the left most child in each level
"""
from trees import TreeNode


def left_children(root, recursive=True):

    def helper_recurse(curr_level):
        curr_level = filter(None, curr_level)
        if not curr_level:
            return
        print(curr_level[0].val)
        next_level = []
        for node in curr_level:
            next_level.append(node.left)
            next_level.append(node.right)
        helper_recurse(next_level)

    if not root:
        return
    helper_recurse([root])


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = n1 = TreeNode(2)
    root.right = n2 = TreeNode(6)
    n2.left = n3 = TreeNode(7)
    n2.right = n4 = TreeNode(8)
    n3.left = TreeNode(9)
    n3.right = TreeNode(10)
    left_children(root)