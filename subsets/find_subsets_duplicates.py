import copy


def find_subsets_duplicates(nums):
    """Brute force approach at the end by removing duplicated by converting to tuples and hashing them"""
    nums = sorted(nums)
    subsets = [[]]
    for num in nums:
        prev_sets = copy.deepcopy(subsets)
        new_sets = [subset + [num] for subset in subsets]
        subsets = prev_sets + new_sets
    uniques = set([tuple(s) for s in subsets])
    return [list(t) for t in uniques]


def find_subsets_duplicates2(nums):
    nums = sorted(nums)
    subsets = [[]]
    for i, num in enumerate(nums):
        prev_sets = copy.deepcopy(subsets)
        if i > 0 and num == nums[i - 1]:  # if num is equal to the prev number, then only add num to the
            # new sets generated in the last iteration
            new_sets = [subset + [num] for subset in new_sets]
        else:
            new_sets = [subset + [num] for subset in subsets]
        subsets = prev_sets + new_sets
    return subsets


if __name__ == '__main__':
    print(find_subsets_duplicates([3, 1, 3]))
    print(find_subsets_duplicates2([3, 1, 3]))
