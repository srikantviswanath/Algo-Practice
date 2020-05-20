def find_subarrays(arr, target):
    """
    Given an unsorted array of positive integers, find all contiguous subarrays whose produce is less
    that given target
    """
    result = []
    if not arr:
        return result
    for left in range(len(arr)):
        product = arr[left]
        right = left
        while product < target:
            result.append(arr[left:right+1])
            right += 1
            if right >= len(arr):
                break
            product *= arr[right]
    return result


if __name__ == '__main__':
    print(find_subarrays(list(range(1, 500)), 30000))