def two_sum(arr, target):
    start, end = 0, len(arr) - 1
    while start < end:
        curr_sum = arr[start] +  arr[end]
        if curr_sum == target:
            return [start, end]
        elif curr_sum > target:
            end -= 1
        else:
            start += 1
    return [-1, -1]


print(two_sum([2, 5, 9, 11], 11))