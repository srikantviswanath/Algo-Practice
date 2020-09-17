from trees import TreeNode, build_binary_tree
from collections import deque


def find_minimum_depth(root: TreeNode) -> int:
    if not root:
        return 0
    min_depth = 1
    q = deque([[root]])
    while q:
        next_level = []
        curr_level = q.popleft()
        for node in curr_level:
            if not node.left and not node.right:
                return min_depth
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        min_depth += 1
        q.append(next_level)


if __name__ == '__main__':
    root = build_binary_tree([])
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))