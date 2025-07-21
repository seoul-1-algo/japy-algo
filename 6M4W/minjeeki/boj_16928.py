from collections import deque 

max_board = 101
max_dice = 6

N, M = map(int, input().split())
visited = [False] * max_board
events = [0] * max_board
deq = deque()
for _ in range(N):
	x, y = map(int, input().split())
	events[x] = y
for _ in range(M):
	u, v = map(int, input().split())
	events[u] = v

visited[1] = True
deq.append((1, 0))

while deq:
    cur_place, cur_cnt = deq.popleft()
    if cur_place == 100:
        print(cur_cnt)
        break

    for dice in range(1, max_dice + 1):
        next_place = cur_place + dice
        if next_place > 100:
            continue

        while events[next_place] != 0:
            next_place = events[next_place]

        if not visited[next_place]:
            visited[next_place] = True
            deq.append((next_place, cur_cnt + 1))
