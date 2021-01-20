def find_all_permutations_iterative(nums):
    if not nums:
        return []
    if len(nums) == 1:
        return [nums]
    perms = [[nums[0]]]
    for num in nums[1:]:
        curr_level = []
        for subset in perms:
            for index, _ in enumerate(subset):
                curr_level.append(subset[:index] + [num] + subset[index:])
            curr_level.append(subset + [num])
        perms = curr_level
    return perms


if __name__ == '__main__':
    print(find_all_permutations_iterative([1, 2, 3]))
