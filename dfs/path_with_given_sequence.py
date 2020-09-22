from collections import deque
from trees import build_binary_tree, is_leaf_node


def find_path(root, sequence):
    """
    Given a binary tree and a number sequence, find if the sequence is present as a
    root-to-leaf path in the given tree.
    """
    seq_q = deque(sequence)

    def helper(root, seq):
        if root.val is None:
            return
        if is_leaf_node(root) and len(seq) == 1 and seq[0] == root.val:
            return True
        msd = seq.popleft()
        if msd == root.val:
            leftret = helper(root.left, seq)
            seq.appendleft(msd)
            rightret = helper(root.right, seq)
            return leftret or rightret
        else:
            return False

    return helper(root, seq_q)


if __name__ == '__main__':
    root = build_binary_tree([1, 0, 1, None, 1, 6, 5])
    print(find_path(root, [1, 1, 6]))
