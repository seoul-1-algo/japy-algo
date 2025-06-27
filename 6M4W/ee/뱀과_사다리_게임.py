# 죄송합니다 어떻게 푸는 지 모르겟어서 블로그도 보고 지피티도 좀 봤습니다. 

import sys
sys.stdin = open('16928.txt')

from collections import deque

N, M = map(int, input().split()) # 사다리 수 N, 뱀의 수 M

movement = [i for i in range(101)]

# 사다리
for _ in range(N):
    x, y = map(int, input().split())
    movement[x] = y

# 뱀
for _ in range(M):
    u, v = map(int, input().split())
    movement[u] = v

visited = [False] * 101
queue = deque([(1, 0)]) # (현재 칸, 주사위 굴린 횟수)

visited[1] = True

while queue:
    now, cnt = queue.popleft()

    if now == 100:
        print(cnt)
        break

    for i in range(1, 7):
        next = now + i
        if next <= 100 and not visited[movement[next]]:
            visited[movement[next]] = True
            queue.append((movement[next], cnt + 1))