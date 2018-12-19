"""
convert a given ternary expression(like in java), convert it into a binary tree

e.g: a?b:c?d:e
output:
     a
  b     c
      d   e
"""
from trees import TreeNode, print_level_order


def ternary_to_binary_tree_iterative(expression):
    if not expression:
        return
    stack = []
    root = TreeNode(expression[0])
    stack.append(root)
    for index in range(1, len(expression)):
        if expression[index] == '?':
            top_element = stack[-1]
            top_element.left = TreeNode(expression[index + 1])
            stack.append(top_element.left)
        elif expression[index] == ':':
            stack.pop()
            last_root = stack.pop()
            last_root.right = TreeNode(expression[index + 1])
            stack.append(last_root.right)
    return root


if __name__ == '__main__':
    root = ternary_to_binary_tree_iterative('a?k?l:m?p:q:b?s?t:u:v')
    print_level_order(root)
