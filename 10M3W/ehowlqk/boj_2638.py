from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

queue = deque([])
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

"""
-1: 외부 공기
0: 내부 공기
1: 치즈
"""

# 외부 공기로 바꾸기
def find_outer_air(r, c, time):
    q = deque([])
    q.append((r, c))
    visited = [[False for _ in range(m)] for _ in range(n)] 
    visited[r][c] = True

    while q:
        row, col = q.popleft()

        graph[row][col] = -1

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            # 치즈라면 C 표시 할말
            if 0 <= nr < n and 0 <= nc < m:
                if graph[nr][nc] == 1 and not changed[nr][nc]:
                    find_melting_cheeze(nr, nc, time)
                # 공기라면 외부공기로 바꿈
                elif graph[nr][nc] == 0 and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = True
            

# C로 표시할 치즈 찾기
def find_melting_cheeze(row, col, time):
    n_air = 0
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == -1:
            n_air += 1
    if n_air >= 2 and not changed[row][col]:
        queue.append((row, col, time+1))
        changed[row][col] = True


changed = [[False for _ in range(m)] for _ in range(n)]
answer = 0

find_outer_air(0, 0, 0) # 맨 처음 외부 공기 구분하기
            
while queue:
    row, col, time = queue.popleft()
    find_outer_air(row, col, time)

    for i in range(4):
        nr, nc = row + dr[i], col + dc[i]
        if 0 <= nr < n and 0 <= nc < m and not changed[nr][nc] and graph[nr][nc] == 1:
            find_melting_cheeze(nr, nc, time)
    answer = max(answer, time)

print(answer)
