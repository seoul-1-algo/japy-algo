from collections import deque

n,m = map(int, input().split())

entire_map = [list(map(int, input().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
check = deque([])
recover = []

for i in range(n):
  for j in range(m):

    if entire_map[i][j] == 2:
      for direction in range(4):
        if 0<= i+dx[direction] < n and 0<= j+dy[direction] < m:
          if entire_map[i+dx[direction]][j+dy[direction]] == 1:
            entire_map[i][j] = 0
            recover=[i+dx[direction],j+dy[direction]]
            entire_map[i+dx[direction]][j+dy[direction]] = -1
            check.append([i+dx[direction],j+dy[direction]])
      while check:
        now = check.popleft()
        for direction in range(4):
          if 0 <= now[0] + dx[direction] < n and 0 <= now[1] + dy[direction] < m:
            if entire_map[now[0] + dx[direction]][now[1] + dy[direction]] == 1:
              entire_map[now[0] + dx[direction]][now[1] + dy[direction]] = entire_map[now[0]][now[1]] -1
              check.append([now[0] + dx[direction],now[1] + dy[direction]])

for i in range(n):
  for j in range(m):
    entire_map[i][j]*=-1

for i in range(n):
  print(*entire_map[i])