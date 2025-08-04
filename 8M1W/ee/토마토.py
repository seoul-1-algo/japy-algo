import sys
sys.stdin = open('7569.txt')

from collections import deque

M, N, H = map(int, input().split()) 

tomatoes = [[list(map(int, input().split())) for _ in range(N)] for __ in range(H)]

di = [1, -1, 0, 0, 0, 0]
dj = [0, 0, 1, -1, 0, 0]
dk = [0, 0, 0, 0, 1, -1]

days = 0 # 모든 토마토가 익을 때 까지 며칠이 걸리는 지
cnt = 0 # 익은 토마토의 수

q = deque([])

for i in range(H):
    for j in range(N):
        for k in range(M):
            if not tomatoes[i][j][k]: # 토마토가 익지 않았다면 패스
                continue

            if tomatoes[i][j][k] == 1: # 토마토가 익었다면
                q.append((i, j, k)) # 큐에 추가

            cnt += 1 # 익은 토마토와 비어있는 칸 세기

if cnt == M * N * H: # 이미 상자안의 토마토가 모두 익어있음
    print(0)
    exit()
    
while q:
    i, j, k = q.popleft()
    for l in range(6):
        ni, nj, nk = i + di[l], j + dj[l], k + dk[l]
        if 0 <= ni < H and 0 <= nj < N and 0 <= nk < M and tomatoes[ni][nj][nk] == 0: # 토마토가 익지 않았다면
            tomatoes[ni][nj][nk] = tomatoes[i][j][k] + 1
            cnt += 1
            q.append((ni, nj, nk))
            days = max(days, tomatoes[ni][nj][nk])

if cnt < M * N * H: #모든 토마토가 익지 못한다면
    print(-1)
else:
    print(days - 1)