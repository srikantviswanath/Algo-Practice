"""
Given a 2-D grid, count the number of paths from top left corner to bottom right corner with the condition that
if there is a 1 in any cell, a path cannot go thru that call. 0 denotes pass; 1 denotes no pass
"""


def unique_paths(grid):
    if not grid:
        return 0
    cache = {}
    m, n = len(grid), len(grid[0])

    def helper(r, c):
        if r < 0 or r >= m or c < 0 or c >= n:
            return 0
        elif grid[r][c] == 1:
            cache[(r, c)] = 0
            return 0
        elif r == 0 and c == 0:
            return 1
        top_ways = helper(r - 1, c) if (r - 1, c) not in cache else cache[(r - 1, c)]
        left_ways = helper(r, c - 1) if (r, c - 1) not in cache else cache[r, c - 1]
        cache[(r, c)] = top_ways + left_ways
        return cache[(r, c)]

    return helper(m - 1, n - 1)


import unittest


class TestUniqePaths(unittest.TestCase):

    def test_all_zeros(self):
        g = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(unique_paths(g), 6)

    def test_1_in_top_row(self):
        g = [
            [0, 0, 1],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(unique_paths(g), 5)

    def test_1_in_center(self):
        g = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        self.assertEqual(unique_paths(g), 2)

if __name__ == '__main__':
    unittest.main()
