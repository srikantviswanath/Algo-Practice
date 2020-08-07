from collections import deque
from typing import List
from trees import TreeNode


def traverse(root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    out = [[root]]
    while True:
        curr_level = out[-1]
        next_level = []
        for node in curr_level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        if not any(next_level):
            return out
        else:
            out.append(next_level)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(traverse(root))

