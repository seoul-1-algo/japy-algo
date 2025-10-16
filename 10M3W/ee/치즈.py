import sys
sys.stdin = open('2638.txt')

from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def is_gonna_melted(r, c):
    cnt = 0

    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == -1:
            cnt += 1

    return cnt >= 2

def check_outter_air(q = deque([(0, 0)])):
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    arr[0][0] = -1

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                visited[nr][nc] = True
                if arr[nr][nc] == 0 or arr[nr][nc] == -1:
                    arr[nr][nc] = -1
                    q.append((nr, nc))

ans = 0
check_outter_air()

# 반복
while True:
    # for row in arr:
    #     print(*row)
    cheeses = deque([]) # 이번 턴에 녹을 치즈들
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1 and is_gonna_melted(r, c):
                cheeses.append((r, c))

    # print(cheeses)
    if not cheeses: # 녹을 치즈가 없으면 끝 !!!!
        break
    
    for r, c in cheeses:
        arr[r][c] = 0
    check_outter_air(cheeses)

    ans += 1

print(ans)