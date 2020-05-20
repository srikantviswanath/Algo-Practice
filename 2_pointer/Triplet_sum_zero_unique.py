from typing import List, Tuple
def triple_sum(arr: List[int]) -> List[Tuple[int]]:
	"""Given an unsorted list of integers, find unique triplets that will sum up to 0"""
	if not arr:
		return []
	triplets = set()
	arr.sort()
	for first, num in enumerate(arr):
		target = -num
		second = first + 1
		third = len(arr) - 1
		while second < third:
			if arr[second] + arr[third] > target:
				third -= 1
			elif arr[second] + arr[third] < target:
				second += 1
			else:
				triplets.add((num, arr[second], arr[third]))
				second += 1
	return list(triplets)

"""
Another approach for uniqueness, without the use of set, is that after sorting - we know all equal numbers would be 
next to each other. So while running the `second` pointer, check if next val is of same val - if yes, then just skip!
"""
