from typing import List
from random import shuffle


def cyclic_sort(nums: List[int]) -> None:
    """
    Given an array of ints from 1 to N where N is len(nums),
    sort them in-place without extra space in O(N)
    """
    if not nums:
        return
    index = 0
    while index < len(nums):
        temp =  nums[index]
        while temp != nums[temp - 1]:
            nums[temp - 1], temp = temp, nums[temp - 1]
        index += 1


if __name__ == '__main__':
    nums = list(range(1, 20))
    shuffle(nums)
    print(nums)
    cyclic_sort(nums)
    print(nums)