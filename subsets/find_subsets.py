import copy


def find_subsets_iterative(nums):
    all_subsets = [[]]
    for num in nums:
        next_level = copy.deepcopy(all_subsets)
        for subset in all_subsets:
            subset.append(num)
            next_level.append(subset)
        all_subsets = next_level
    return all_subsets


def find_subsets_recursive(nums):
    if not nums:
        return [[]]
    prev_layer = find_subsets_recursive(nums[1:])
    curr_layer = copy.deepcopy(prev_layer)
    return curr_layer + [subset + [nums[0]] for subset in prev_layer]


if __name__ == '__main__':
    print(find_subsets_iterative([1, 5, 3]))
    print(find_subsets_recursive([1, 5, 3]))


