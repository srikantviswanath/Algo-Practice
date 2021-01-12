from trees import TreeNode, build_binary_tree
from collections import deque


class TreeNodeWithNext(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.next = None
        self.val = val


def print_level_order(root):
    nextLevelRoot = root
    while nextLevelRoot:
        current = nextLevelRoot
        nextLevelRoot = None
        while current:
            print(str(current.val) + " ", end='')
            if not nextLevelRoot:
                if current.left:
                    nextLevelRoot = current.left
                elif current.right:
                    nextLevelRoot = current.right
            current = current.next


def connect_successor(root: TreeNode) -> None:
    if not root:
        return
    q = deque([[root]])
    while q:
        current_level = q.popleft()
        next_level = []
        for node in current_level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        if not any(next_level):
            return
        for left, right in list(zip(next_level, next_level[1:])):
            left.next = right
        q.append(next_level)


if __name__ == '__main__':
    root = build_binary_tree([12, 7, 1, 9, None, 10, 5])
    connect_successor(root)
    print_level_order(root)
