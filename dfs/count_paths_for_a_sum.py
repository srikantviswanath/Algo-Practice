"""Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all
the node values of each path equals ‘S’. Please note that the paths can start or end at any
node but all paths must follow direction from parent to child (top to bottom)"""

from trees import TreeNode, build_binary_tree
from typing import List


def count_paths(root: TreeNode, target: int) -> int:
    count = {'count': 0}

    def helper(root: TreeNode, target: int, current_path: List[int]) -> None:
        if not root:
            return
        i = 0
        if current_path:
            while target < root.val:
                target += current_path[i]
                i += 1
            if target == root.val:
                count['count'] += 1
        target -= root.val
        current_path = current_path[i+1:] if i != 0 else current_path
        helper(root.left, target, current_path + [root.val])
        helper(root.right, target, current_path + [root.val])

    helper(root, target, [])
    return count['count']


if __name__ == '__main__':
    root = build_binary_tree([12, 7, 1, None, 4, 10, 5])
    print(count_paths(root, 6))
