def spiralOrder(matrix):
    out = []
    R, C = len(matrix), len(matrix[0])
    count = 0
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    r, c = 0, 0
    d = 0
    while count < R * C:
        while r < R and c < C and matrix[r][c] != 'X':
            out.append(matrix[r][c])
            count += 1
            matrix[r][c] = 'X'
            d_r, d_c = dirs[d % 4]
            r, c = r + d_r, c + d_c
        r, c = r - dirs[d % 4][0], c - dirs[d % 4][1]
        d += 1
        r, c = r + dirs[d % 4][0], c + dirs[d % 4][1]
    return out


if __name__ == '__main__':
    print(spiralOrder([
        [1, 2, 3, 2],
        [4, 5, 6, 4],
        [7, 8, 9, 7]
    ]))