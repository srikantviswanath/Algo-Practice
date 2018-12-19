def binary_search(array, target):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binary_search_recursive(array, target):

    def helper(low, high):
        if low > high:
            return -1
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        return helper(low, high)

    return helper(0, len(array) - 1)

if __name__ == '__main__':
    print(binary_search(range(10**10), 77))
    print(binary_search_recursive(range(100, 10**10), 200))