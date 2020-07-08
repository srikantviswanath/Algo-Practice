from typing import List


def merge_interval(arr: List[List[int]]):
    """
    Given a list of intervals, return a list of merged intervals
    """
    if not arr:
        return []
    arr.sort(key=lambda interval: interval[0])
    output = []
