from collections import deque

MAX_NUM = 100000
subin, sister = map(int, input().split())
road = [-1] * (MAX_NUM + 1)
road[subin] = 0
deq = deque([subin])

while deq:
    cur = deq.popleft()
    cur_t = road[cur]
    if cur == sister:
        print(cur_t)
        break
    for nxt, nxt_t in ((cur + 1, cur_t + 1), (cur - 1, cur_t + 1), (cur * 2, cur_t)):
        if 0 <= nxt <= MAX_NUM and (road[nxt] == -1 or road[nxt] > nxt_t):
            if nxt == cur * 2:
                deq.appendleft(nxt)
                road[nxt] = nxt_t
            else:
                deq.append(nxt)
                road[nxt] = nxt_t