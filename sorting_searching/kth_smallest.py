import heapq


def kth_smallest_min_heap(array, k):
    """using min heap - O(kLogN), O(N)"""
    if not array:
        return
    if k > len(array):
        raise ValueError
    heapq.heapify(array)
    out = None
    for i in range(k):
        out = heapq.heappop(array)
    return out


def kth_smallest_max_heap(array, k):
    """using maxheap = O(Nlogk), O(k)"""
    if not array:
        return
    if k > len(array):
        raise ValueError
    heap = [-num for num in array[:k]]
    heapq.heapify(heap)
    for num in range(k, len(array)):
        neg = -array[num]
        if neg >heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, neg)
    return -heap[0]


def quick_select(array, k):

    def partiton(arr):
        pivot = 0
        low, high = 1, len(arr) - 1
        while low < high:
            while arr[pivot] > arr[low]:
                low += 1
            while arr[pivot] < arr[high]:
                high -= 1
            if high < low:
                break
            arr[high], arr[low] = arr[low], arr[high]
            low += 1
            high -= 1
        arr[pivot], arr[high] = arr[high], arr[pivot]
        return arr, high + 1

    if not array:
        return
    if k > len(array) or k <= 0:
        raise ValueError
    array, pivot = partiton(array)
    while pivot != k:
        if pivot < k:
            array = array[pivot:]
            k = k - pivot
        elif pivot > k:
            array = array[:pivot-1]
        array, pivot = partiton(array)
    return array[pivot - 1]








if __name__ == '__main__':
    print(kth_smallest_min_heap([4, 6, 3, 2, 7, 8, 10, 9, 99, 87, 1, -1], 3))
    print(kth_smallest_max_heap([4, 6, 3, 2, 7, 8, 10, 9, 99, 87, 1, -1], 3))
    print(quick_select([12, 11, 6, 4, 7, 9, 2, 3, 19, 16], 5))