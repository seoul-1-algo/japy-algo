def dfs(r, c):
    if checked[r][c]:
        return 0
    if visited[r][c]:
        return 1

    visited[r][c] = True

    nr, nc = r, c
    
    dir = dirs[r][c]
    if dir == 'U':
        nr = r-1
    elif dir == 'D':
        nr = r+1
    elif dir == 'L':
        nc = c-1
    else:
        nc = c+1
    
    result = dfs(nr, nc)
    checked[r][c] = True
    return result


N, M = map(int, input().split())
dirs = [list(input()) for _ in range(N)]

visited = [[False for _ in range(M)] for _ in range(N)]     # dfs 시 방문 여부 
checked = [[False for _ in range(M)] for _ in range(N)]     # SAFE ZONE으로 향하는 지

sz = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            sz += dfs(i, j)

print(sz)
