def rotate_array(array, K):
    N = len(array)
    for i in range(gcd(N, K)):
        j = i
        buffer = array[i]
        while True:
            if j + K >= N:
                target = (j + K) % N
            else:
                target = j + K
            array[target], buffer = buffer, array[target]
            if target == i:
                break
            j = target
    return array


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    print(rotate_array([1, 2, 3, 4, 5, 6, 7, 8], 5))