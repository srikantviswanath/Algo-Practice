def remove_duplicates(arr):
    """given an array of sorted numbers, return the len of the array after removing duplicates.
    Cannot use extra space. E.g remove_duplicates([2, 3, 3, 3, 6, 9, 9]) -> 4"""
    if not arr:
        return 0
    last_unique = None
    ans = 0
    for curr in range(len(arr)):
        if arr[curr] != last_unique:
            ans += 1
            last_unique = arr[curr]
    return ans


print(remove_duplicates([2, 3, 3, 4,  4, 9, 10, 11]))