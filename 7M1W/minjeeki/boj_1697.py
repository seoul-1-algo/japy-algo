# 숨바꼭질
from collections import deque

MAX_N = 100001
subin, sister = map(int, input().split())

road = [-1] * (MAX_N + 1)
road[subin] = 0

deq = deque([subin])

while deq:
    cur = deq.popleft()
    if cur == sister:
        print(road[cur])
        break
    for next_move in (cur + 1, cur - 1, cur * 2):
        if 0 <= next_move < MAX_N and road[next_move] == -1:
            road[next_move] = road[cur] + 1
            deq.append(next_move)
