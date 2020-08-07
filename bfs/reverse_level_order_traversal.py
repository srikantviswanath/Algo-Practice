from typing import List
from trees import TreeNode
from collections import deque


def reverse_level_order(root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    out = deque([[root]])
    while True:
        curr_level = out[0]
        next_level = []
        for node in curr_level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        if not any(next_level):
            return list(out)
        else:
            out.appendleft(next_level)


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(reverse_level_order(root))