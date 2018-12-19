from collections import defaultdict
from trees import build_binary_tree


def print_vertical_order(root):
    if not root:
        return
    dist_from_center_map = defaultdict(list)
    def dfs(node, dist):
        dist_from_center_map[dist].append(node.val)
        if node.left:
            dfs(node.left, dist - 1)
        if node.right:
            dfs(node.right, dist + 1)
    dfs(root, 0)
    min_dist, max_dist = min(dist_from_center_map), max(dist_from_center_map)
    for num in range(min_dist, max_dist + 1):
        print(dist_from_center_map[num])


if __name__ == '__main__':
    root = build_binary_tree([1, 2])
    print_vertical_order(root)