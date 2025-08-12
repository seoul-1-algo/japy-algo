import sys
sys.stdin = open('14940.txt')

from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(i, j):
    queue = deque([]) 
    queue.append((i, j))

    visited = [[0] * m for _ in range(n)]

    while queue:
        r, c = queue.popleft()
        
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]

            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and arr[nr][nc] == 1:
                queue.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
    
    return visited
           

n, m = map(int, input().split()) # 지도의 크기 (세로 크기 n, 가로 크기 m)
arr = [list(map(int, input().split())) for _ in range(n)] # 지도

# 목표 지점에서 각 지점까지의 거리 
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            answer = bfs(i, j)
            break

# 원래 갈 수 있는 땅인데 도달할 수 없었다면 -1
for i in range(n):
    for j in range(m):
        if answer[i][j] == 0 and arr[i][j] != 0 and arr[i][j] != 2:
            answer[i][j] = -1

# 정답 출력
for row in answer:
    print(*row)