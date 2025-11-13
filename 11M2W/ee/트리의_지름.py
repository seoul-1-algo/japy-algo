import sys
sys.stdin = open('1167.txt')

from collections import deque

N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N):
    temp = list(map(int, input().split()))
    node = temp[0]
    for i in range(1, len(temp)-1, 2):
        graph[node].append((temp[i], temp[i+1]))

def bfs(s):
    q = deque([s])
    
    dist = [-1] * (N+1)
    dist[s] = 0

    max_dist = 0
    max_dist_node = 0

    while q:
        cur = q.popleft()

        if dist[cur] > max_dist:
            max_dist = dist[cur]
            max_dist_node = cur

        for nxt, cost in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + cost
                q.append(nxt)

    return max_dist_node, max_dist

node, _ = bfs(1)
_, ans = bfs(node)

print(ans)