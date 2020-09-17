from typing import List
from trees import TreeNode
from collections import deque


def find_level_averages(root: TreeNode) -> List[float]:
    if not root:
        return []
    out = []
    q = [root]
    while q:
        next_level = []
        out.append(sum(item.val for item in q) / len(q))
        for node in q:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        q = []
        if next_level:
            q = next_level
    return out


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(find_level_averages(root))
