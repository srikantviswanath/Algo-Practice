def smallest_diff(arr1, arr2):
    if not arr1 or not arr2:
        return float('inf')
    ans = float('inf')
    arr2.sort()
    arr1.sort()
    p1, p2 = 0, 0
    while p1 < len(arr1) and p2 <len(arr2):
        diff = abs(arr2[p2] - arr1[p1])
        ans = min(ans, diff)
        if arr1[p1] < arr2[p2]:
            p1 += 1
        else:
            p2 += 1
    return ans

if __name__ == '__main__':
    print(smallest_diff([1], [2]))