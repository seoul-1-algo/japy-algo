N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

for a in range(N):
    for b in range(N):
        for c in range(N):
            if matrix[b][a] and matrix[a][c]:
                matrix[b][c] = 1

for row in matrix:
    print(*row)
