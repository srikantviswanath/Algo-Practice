def four_sum(arr: [int], target: int) -> [[int]]:
    """Given an array of integers, find unique quadruplets which add upto the given target number"""
    """
    O(N^2LogN) Time, O(N^2) space.
    Get an aux array which keeps the pairwise sums of all numbers -> O(N^2) space and time
    Sort this aux array -> O(2N^2LogN) -> O(N^2LogN)
    Do a 2 pointer approach from left and right. Make sure to not count duplicates by maintaining a set of frozensets as
    the final answer
    """
    if not arr:
        return []
    pair_sums = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            pair_sums.append((arr[i] + arr[j], i, j))
    pair_sums.sort(key=lambda x: x[0])
    left, right = 0, len(pair_sums) - 1
    ans = set()
    while left <= right:
        curr_sum = pair_sums[left][0] + pair_sums[right][0]
        if curr_sum == target:
            quad = {pair_sums[left][1], pair_sums[left][2], pair_sums[right][1], pair_sums[right][2]}
            if len(quad) == 4:
                ans.add(frozenset(quad))
            left += 1
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return [list(q) for q in ans]


print(four_sum([4, 1, 2, -1, 1, -3], 1))