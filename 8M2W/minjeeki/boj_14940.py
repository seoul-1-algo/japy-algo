# 실버 1 / 14940 쉬운 최단거리 / 메모리 41588: KB, 시간 : 696ms
from collections import deque

n, m = map(int, input().split()) # 2 <= n(지도 세로) <= 1000, 2 <= m(지도 가로) <= 1000

# 갈 수 없는 땅 0 / 갈 수 있는 땅 1 / 목표지점 2
board = [[] for _ in range(n)]
# 목표지점 찾으면서 board 입력값 받기
for i in range(n):
    board[i] = list(map(int, input().split()))
    for j in range(m):
        if board[i][j] == 2:
            start_x, start_y = i, j

# 목표지점부터 BFS 탐색하면서 new_board 값 갱신
new_board = [[-1] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            new_board[i][j] = 0

deq = deque([(start_x, start_y)])
new_board[start_x][start_y] = 0
directions = [(1,0), (-1,0), (0,1), (0,-1)]

while deq:
    cur_x, cur_y = deq.popleft()
    for dx, dy in directions:
        next_x, next_y = cur_x + dx, cur_y + dy
        if 0 <= next_x < n and 0 <= next_y < m:
            if board[next_x][next_y] != 0 and new_board[next_x][next_y] == -1:
                new_board[next_x][next_y] = new_board[cur_x][cur_y] + 1
                deq.append([next_x, next_y])

for i in range(n):
    print(*new_board[i])
