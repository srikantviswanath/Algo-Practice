def interspersed_search(list_of_strings, target):
    """Given a sorted list of strings interspersed with empty strings, find a target string"""
    if not target:
        raise ValueError
    low, high = 0, len(list_of_strings) - 1
    while low <= high:
        mid = (low + high) // 2
        if list_of_strings[mid] == target:
            return mid
        if not list_of_strings[mid]:
            mid, mid_minus_1 = scan(list_of_strings, mid, low, high)
        else:
            mid, mid_minus_1 = mid, mid - 1
        if list_of_strings[mid] > target:
            high = mid_minus_1
        elif list_of_strings[mid] < target:
            low = mid + 1
        else:
            return mid
    return -1



def scan(array, empty_str_index, start, end):
    low, high = empty_str_index, empty_str_index
    while not array[low] and low >= start:
        low -= 1
    while not array[high] and high <= end:
        high += 1
    return high, low


if __name__ == '__main__':
    print(interspersed_search(['', 'apple', 'attention', '', '', 'cat', '', 'cot', 'eagle', '', '', '', 'farro', 'ferret', '', 'tom'], 'ferret'))