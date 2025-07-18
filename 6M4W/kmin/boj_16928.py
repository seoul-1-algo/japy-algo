import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
# 사다리던 뱀이던 움직이는 방식
move = {}
for _ in range(N + M):
    x, y = map(int, input().split())
    move[x] = y
# 빈 보더 와 visited 만들기
arr = [0] * 101
visited = [0] * 101
# bfs
q = deque()
q.append(1)
visited[1] = True
while q:
    # 현재 위치
    current = q.popleft()
    # 주사위 1부터 6까지
    for i in range(1, 7):
        next = current + i  # 다음 칸
        if 0 < next <= 100 and not visited[next]:   # 다음 칸이 보드 안에 있고, 방문 안했으면
            if next in move:    # 뱀과 사다리 안에 잇으면
                next = move[next]   # 다음칸은 뱀과 사다리의 밸류 값이 된다
            if not visited[next]:   # 방문 처리 안되어 있으면
                q.append(next)      # 큐에 추가
                visited[next] = True    # 방문처리
                arr[next] = arr[current] + 1    # 다음 칸은 현재 칸보다 주사위 굴림 수 + 1
print(arr[100])
        


