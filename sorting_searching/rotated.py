def rotated_binary_search(array, target):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == array[mid]:
            return mid
        if array[mid] <= array[high]:  # right half is sorted correct
            if array[mid] < target <= array[high]:
                low = mid + 1
            else:
                high = mid - 1
        else:  # left half is sorted correct
            if array[low] <= target < array[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return -1


if __name__ == '__main__':
    arr = range(10 ** 4)
    arr = list(arr[70:]) + list(arr[:70])
    print(rotated_binary_search(arr, 71))
