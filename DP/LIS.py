"""
Longest increasing sub-sequence. This is a O(N^2) approach using DP
"""

def LIS(nums):
    if not nums:
        return 0
    elif len(nums) == 1:
        return 1
    output = 1
    cache = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[j] < nums[i]:
                cache[i] = max(cache[i], cache[j] + 1)
        output = max(output, cache[i])
    return output


import unittest


class TestLIS(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(LIS([]), 0)

    def test_one_elt(self):
        self.assertEqual(LIS([1]), 1)

    def test_all_decreasing(self):
        self.assertEqual(
            LIS([7, 6, 5, 4, 3, 2, 1]),
            1
        )

    def test_all_increasing(self):
        self.assertEqual(
            LIS([1, 2, 3, 4, 5, 6, 7]),
            7
        )

    def test_randomized(self):
        self.assertEqual(
            LIS([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]),
            6
        )


if __name__ == '__main__':
    unittest.main()