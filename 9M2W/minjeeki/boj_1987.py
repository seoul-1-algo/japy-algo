import sys
from collections import deque


data = sys.stdin.read().strip().split("\n")
R, C = map(int, data[0].split())
table = [i for i in data[1:]]
visited = [[False]*C for _ in range(R)]
q = deque([[(0,0),table[0][0]]])
visited[0][0] = True
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0


def dfs(x, y, history):
    global answer
    if len(history) > answer:
        answer = len(history)

    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and table[nx][ny] not in history:
            if not visited[nx][ny]:
                dfs(nx, ny, history + table[nx][ny])
    
    visited[x][y] = False

dfs(0, 0, table[0][0])
print(answer)