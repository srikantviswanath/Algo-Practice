from typing import List
from trees import TreeNode


def zig_zag_traversal(root: TreeNode) -> List[List[TreeNode]]:
    if not root:
        return []
    out = [[root]]
    curr = 1
    while True:
        curr_level = out[-1]
        next_level = []
        for node in curr_level[::-1]:
            if curr % 2 == 1:
                if node.right:
                    next_level.append(node.right)
                if node.left:
                    next_level.append(node.left)
            if curr % 2 == 0:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
        if not any(next_level):
            return out
        out.append(next_level)
        curr += 1


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print(zig_zag_traversal(root))
