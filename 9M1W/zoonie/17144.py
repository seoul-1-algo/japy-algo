import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(r)]

for i in range(r):
    if field[i][0] == -1:
        machine_up = i
        machine_down = i + 1
        break

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(t):
    dust_diffusion = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if field[i][j] > 0:
                amount = field[i][j] // 5
                cnt = 0
                for d in range(4):
                    ni, nj = i+dy[d], j+dx[d]
                    if 0 <= ni < r and 0 <= nj < c and field[ni][nj] != -1:
                        dust_diffusion[ni][nj] += amount
                        cnt += 1
                dust_diffusion[i][j] -= amount * cnt

    for i in range(r):
        for j in range(c):
            field[i][j] += dust_diffusion[i][j]

    new_field = [row[:] for row in field]

    x = machine_up
    for i in range(x-1, 0, -1):
        new_field[i][0] = field[i-1][0]
    for j in range(c-1):
        new_field[0][j] = field[0][j+1]
    for i in range(x):
        new_field[i][c-1] = field[i+1][c-1]
    for j in range(c-1, 1, -1):
        new_field[x][j] = field[x][j-1]
    new_field[x][1] = 0

    x = machine_down
    for i in range(x+1, r-1):
        new_field[i][0] = field[i+1][0]
    for j in range(c-1):
        new_field[r-1][j] = field[r-1][j+1]
    for i in range(r-1, x, -1):
        new_field[i][c-1] = field[i-1][c-1]
    for j in range(c-1, 1, -1):
        new_field[x][j] = field[x][j-1]
    new_field[x][1] = 0

    field = new_field

ans = 0
for i in range(r):
    for j in range(c):
        if field[i][j] > 0:
            ans += field[i][j]
print(ans)
