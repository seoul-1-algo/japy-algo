from collections import deque

dh = (0, 0, 0, 0, 1, -1)
dn = (1, -1, 0, 0, 0, 0)
dm = (0, 0, 1, -1, 0, 0)
def ft_bfs(deq, cnt_not_ripe):
    if cnt_not_ripe == 0:
        return 0
    dates = 1
    len_date = len(deq)
    visited = set()
    while deq:
        ch, cn, cm = deq.popleft()
        len_date -= 1
        for i in range(6):
            nh = ch + dh[i]
            nn = cn + dn[i]
            nm = cm + dm[i]
            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and \
                tomatos[nh][nn][nm] == 0 and (nh, nn, nm) not in visited:
                tomatos[nh][nn][nm] = 1
                visited.add((nh, nn, nm))
                cnt_not_ripe -= 1
                deq.append((nh, nn, nm))
        if len_date == 0 and cnt_not_ripe != 0:
            dates += 1
            len_date = len(deq)
        elif cnt_not_ripe == 0:
            return dates
    return -1


M, N, H = map(int, input().split())
cnt_not_ripe = 0
tomatos = []
deq = deque()
for h in range(H):
    tomato_floor = []
    for n in range(N):
        tomato_line = list(map(int, input().split()))
        cnt_not_ripe += tomato_line.count(0)
        tomato_floor.append(tomato_line)
        for m in range(M):
            if tomato_line[m] == 1:
                deq.append((h, n, m))
    tomatos.append(tomato_floor)
dates = ft_bfs(deq, cnt_not_ripe)
print(dates)
