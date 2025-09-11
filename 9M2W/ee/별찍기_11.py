import sys
sys.stdin = open('2448.txt')

N = int(input())
W = 2 * N

stars = [[' '] * W for _ in range(N)]

def star(r, c, n):
    if n == 3:
        stars[r][c] = '*'
        stars[r+1][c-1] = stars[r+1][c+1] = '*'
        stars[r+2][c-2] = stars[r+2][c-1] = stars[r+2][c] = stars[r+2][c+1] = stars[r+2][c+2] = '*'
        return

    star(r, c, n//2)
    star(r + n//2, c - n//2, n//2)
    star(r + n//2, c + n//2, n//2)

star(0, N-1, N)
for row in stars:
    print(''.join(row))