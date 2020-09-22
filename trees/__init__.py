class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __bool__(self):
        return bool(self.val)

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self)



def is_leaf_node(node: TreeNode):
    return not node.left and not node.right


def build_binary_tree(level_order_nodes):
    """
    Given a list of nodes in level order, from left to right - build a binary tree
    :param [int] array:
    :return TreeNode: root of the tree
    """
    if not level_order_nodes:
        return

    def helper(prev_level, index):
        if not filter(None, prev_level) or index >= len(level_order_nodes):
            return
        next_level = []
        for node in prev_level:
            if index < len(level_order_nodes):
                node.left = TreeNode(level_order_nodes[index])
                index += 1
                next_level.append(node.left)
            if index < len(level_order_nodes):
                node.right = TreeNode(level_order_nodes[index])
                index += 1
                next_level.append(node.right)
        helper(next_level, index)

    root = TreeNode(level_order_nodes[0])
    helper([root], 1)
    return root


def print_level_order(root):
    if not root:
        return

    def helper(curr_level):
        curr_level = list(filter(None, curr_level))
        if not curr_level:
            return
        next_level = []
        for node in curr_level:
            print(node.val, end=', ')
            next_level.append(node.left)
            next_level.append(node.right)
        helper(next_level)

    helper([root])


def print_pre_order(root):
    if not root:
        return
    print(root.val)
    print_pre_order(root.left)
    print_pre_order(root.right)


if __name__ == '__main__':
    level_ordered_str = [10, 7, 8, 6, None, 2, 3, None, None, None, None, 4]
    root = build_binary_tree(level_ordered_str)
    print_pre_order(root)
