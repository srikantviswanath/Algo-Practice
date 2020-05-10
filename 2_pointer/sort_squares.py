import unittest


def sort_squares(arr):
    """
    Given a sorted array of negative and positive numbers, return the sorted array of their squares
    e.g. [-4, -2, 0, 1, 3] -> [0, 1, 4, 9, 16]
    """
    if not arr:
        return []
    if arr[0] >= 0:
        return [num ** 2 for num in arr]
    if arr[-1] <= 0:
        return [num ** 2 for num in arr[::-1]]
    ans = []
    for right, num in enumerate(arr):
        if num >= 0:
            left = right - 1
            break
    while left > -1 and right < len(arr):
        if abs(arr[left]) > abs(arr[right]):
            ans.append(arr[right] ** 2)
            right += 1
        elif abs(arr[left]) <= abs(arr[right]):
            ans.append(arr[left] ** 2)
            left -= 1
    if left > -1:
        ans.extend([n ** 2 for n in arr[:left+1][::-1]])
    elif right < len(arr):
        ans.extend([n ** 2 for n in arr[right:]])
    return ans


class TestSortSquares(unittest.TestCase):

    def test_array_all_positive(self):
        arr = [2, 3, 5, 6]
        self.assertEqual(
            sort_squares(arr),
            [4, 9, 25, 36]
        )

    def test_array_of_all_negative(self):
        arr = [-4, -3, -2, -1]
        self.assertEqual(
            sort_squares(arr),
            [1, 4, 9, 16]
        )

    def test_empty_array(self):
        self.assertEqual(sort_squares([]), [])

    def test_mix(self):
        arr = [-6, -3, -1, 2, 4, 5]
        self.assertEqual([1, 4, 9, 16, 25, 36], sort_squares(arr))

    def test_mix_with_0(self):
        arr = [-3, -1, 0, 1, 5]
        self.assertEqual([0, 1, 1, 9, 25], sort_squares(arr))


if __name__ == '__main__':
    unittest.main()