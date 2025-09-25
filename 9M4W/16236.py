from collections import deque

n = int(input())

sea = [list(map(int,input().split())) for i in range(n)]

now_i, now_j = 0,0

for i in range(n):
    for j in range(n):
        if sea[i][j] == 9:
            sea[i][j] = 0
            now_i = i
            now_j = j

shark_size = 2
hungry = 2

dx = [1,0,0,-1]
dy = [0,-1,1,0]
t = 0

visited = [[False]*n for _ in range(n)]
visited[now_i][now_j] = True
now = deque([[now_i,now_j,0]])

while now:
    now_shark = now.popleft()
    shark_i, shark_j,now_t = now_shark[0], now_shark[1], now_shark[2]
    
    if sea[shark_i][shark_j] != 0 and sea[shark_i][shark_j] < shark_size:
        hungry-=1
        sea[shark_i][shark_j] = 0
        if hungry == 0:
            shark_size+=1
            hungry = shark_size
        t += now_t
        # ★ 새 BFS를 시작할 때 visited 초기화 필수
        visited = [[False]*n for _ in range(n)]
        visited[shark_i][shark_j] = True
        now = deque([[shark_i, shark_j, 0]])
        continue

    for i in range(4):
        #유효한 칸인지 확인
        if 0<= shark_i+dx[i] < n and 0<=shark_j+dy[i]<n:
            #갈 수 있는 칸인지 확인
            if sea[shark_i+dx[i]][shark_j+dy[i]] <= shark_size and not visited[shark_i+dx[i]][shark_j+dy[i]]:
                visited[shark_i+dx[i]][shark_j+dy[i]] = True
                now.append([shark_i+dx[i],shark_j+dy[i],now_t+1])

print(t)
