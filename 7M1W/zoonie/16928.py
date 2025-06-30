from collections import deque
n = 100001

graph = [-1 for i in range(n)]

now, goal = map(int, input().split())

graph[now] = 0

check = deque([now])

while True:
    nownum = check.popleft()
    if nownum == goal:
        break
    can_be_next = []
    if nownum + 1 < n:
        can_be_next.append(nownum + 1)
    if nownum - 1 >= 0:
        can_be_next.append(nownum - 1)
    if nownum * 2 < n:
        can_be_next.append(nownum * 2)
    for each in can_be_next:
        if graph[each] == -1:
            graph[each] = graph[nownum] + 1
            check.append(each)

print(graph[goal])