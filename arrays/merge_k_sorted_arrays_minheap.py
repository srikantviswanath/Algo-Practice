import heapq
import unittest


class SortedLists(object):

    def __init__(self, arrays):
        self.total_elements = sum([len(arr) for arr in arrays])
        self.arrays = list(filter(None, arrays))
        self.heap = [(arr[0], index, 0) for index, arr in enumerate(self.arrays)] if self.arrays else []
        heapq.heapify(self.heap)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.has_next():
            raise StopIteration
        min_elt, array_index, elt_index = heapq.heappop(self.heap)
        if elt_index < len(self.arrays[array_index]) - 1:
            heapq.heappush(self.heap, (self.arrays[array_index][elt_index + 1], array_index, elt_index + 1))  # IndexError?
        self.count += 1
        return min_elt

    def has_next(self):
        return self.count < self.total_elements


class TestSortListsIterator(unittest.TestCase):

    def test_all_empty_lists(self):
        iterator = SortedLists([[], [], []])
        output = [num for num in iterator]
        self.assertListEqual(output, [])

    def test_some_empty_lists(self):
        iterator = SortedLists([[3, 8, 9], [], [], [1, 4, 5, 15]])
        output = [num for num in iterator]
        self.assertListEqual(output, [1, 3, 4, 5, 8, 9, 15])

    def test_all_non_empty(self):
        iterator = SortedLists([[3, 8, 9], [9, 10], [1, 100, 200], [1, 4, 5, 15]])
        output = [num for num in iterator]
        self.assertListEqual(output, [1, 1, 3, 4, 5, 8, 9, 9, 10, 15, 100, 200])

if __name__ == '__main__':
    unittest.main()
