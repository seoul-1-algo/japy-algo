import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
q = deque()
visited = [-1] * 100001  # 10만까지니깐
visited[N] = 0  # 시작 위치 초기화
q.append(N)
while q:    # bfs 시작
    x = q.popleft() # 현재 위치

    if x == K:  # 동생위치에 도착하면
        print(visited[x])   # 걸린 시간 출력
        break   # 종료

    for y in (x - 1, x + 1, 2 * x): # 이동할 수 있는 3가지 경우
        if 0 <= y <= 100000 and visited[y] == -1:   # 유효범위내 방문안했다면
            if y == 2 * x:  # 순간이동 시 0초
                visited[y] = visited[x]
                q.appendleft(y) # 가중치가 0이므로 앞쪽에 넣는다 0-1bfs
            else:   # 1초 이동
                 visited[y] = visited[x] + 1
                 q.append(y)    # 가중치가 1이므로 뒤쪽에 넣음