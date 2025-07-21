from collections import deque

n,k = map(int,input().split())

cost = [100001 for i in range(100001)]
cost[n] = 0
queue = deque([[n,0]])

while queue:
    now = queue.popleft()
    if now[0]*2 <= 100000:
        if cost[now[0]*2] > now[1]:
            cost[now[0]*2] = now[1]
            queue.append([now[0]*2,now[1]])
    if now[0]>0:
        if cost[now[0]-1] > now[1]+1:
            cost[now[0]-1] = now[1]+1
            queue.append([now[0]-1,now[1]+1])
    if now[0] < 100000:
        if cost[now[0]+1] > now[1]+1:
            cost[now[0]+1] = now[1]+1
            queue.append([now[0]+1, now[1]+1])

print(cost[k])