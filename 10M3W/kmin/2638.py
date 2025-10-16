from collections import deque
import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]    # 0 : 공기 , 1 : 치즈

# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
 
# 외부 공기와 접촉하는 부분 탐색
def bfs():
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((0, 0))    #$ 가장자리는 무조건 공기
    visited[0][0] = True
 
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]: # 격자 범위 내 & 아직 방문하지 않은 칸일 경우
                if cheese[nx][ny] >= 1:     # 이웃이 치즈라면, + 1 (공기 1번 접촉 : 2, 2번 첩촉 3 ...)
                    cheese[nx][ny] += 1     # 치즈는 공기가 아니므로 큐에 추가 x
                else:   # 공기면 계속 ㄱㄱ
                    q.append((nx, ny))
                    visited[nx][ny] = True
 
# 외부 공기와 2변 이상 접촉한 부분을 제거
def melt_cheese():
    melted = 0
    # 3이상 : 외부 공기 2번 이상 접촉, 2 : 1로, 1 그대로 둠
    for i in range(n):
        for j in range(m):
            if cheese[i][j] >= 3:   # 3 완전 녹음
                cheese[i][j] = 0
                melted += 1
            elif cheese[i][j] == 2:
                cheese[i][j] = 1    
    return melted
 
time = 0
while True:
    bfs()
    melted = melt_cheese()
    
    if melted:
        # 이번에 하나라도 치즈가 녹았으면 시간 + 1
        time += 1
    else: # 더 이상 녹일 부분이 없다면 시간 출력
        print(time)
        break
