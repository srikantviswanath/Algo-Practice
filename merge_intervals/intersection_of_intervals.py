from typing import List


def intersection(arr1: List[List[int]], arr2: List[List[int]]) -> List[List[int]]:
    """
        Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint
        intervals sorted on their start time.
    """
    if not arr1 or not arr2:
        return []
    first, second = 0, 0
    output = []
    while first < len(arr1) and second < len(arr2):
        lower, higher = (arr1[first], arr2[second]) if arr1[first][0] < arr2[second][0] else (arr2[second], arr1[first])
        if higher[0] <= lower[1]:
            output.append([higher[0], min(lower[1], higher[1])])
        if arr1[first][1] < arr2[second][1]:
            first += 1
        else:
            second += 1
    return output


if __name__ == '__main__':
    print(intersection(
        [[1, 3], [5, 7], [9, 12]],
        [[5, 10]]
    ))