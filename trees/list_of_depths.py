"""
4.3 Given a binary tree, design an algorithm which creates a list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
"""

def list_of_depths(root):
    if not root:
        return
    out = []
    def helper(node, level):
        pass