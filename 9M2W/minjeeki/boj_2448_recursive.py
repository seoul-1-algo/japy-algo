def draw(arr, r, c, h):
    if h == 3:
        arr[r][c] = '*'
        arr[r+1][c-1] = arr[r+1][c+1] = '*'
        for j in range(-2, 3):
            arr[r+2][c+j] = '*'
        return
    half = h // 2
    # 위
    draw(arr, r, c, half)
    # 왼쪽 아래
    draw(arr, r + half, c - half, half)
    # 오른쪽 아래
    draw(arr, r + half, c + half, half)

N = int(input())
W = 2 * N - 1
arr = [[' ']*W for _ in range(N)]
draw(arr, 0, N-1, N)
print('\n'.join(''.join(row) for row in arr))
