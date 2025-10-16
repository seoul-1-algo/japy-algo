import sys
sys.stdin = open('1238.txt')

import heapq

INF = 1e9

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

def dijkstra(start):
    distance = [INF] * (N+1)

    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

total = [0] * (N+1)
distances = dijkstra(X)
for i in range(1, N+1):
    if distances[i] != INF:
        total[i] = distances[i] + dijkstra(i)[X]

print(max(total))


# INF = 1e10

# N, M, X = map(int, input().split())
# graph = [[INF] * (N+1) for _ in range(N+1)]

# for a in range(1, N+1):
#     for b in range(1, N+1):
#         if a == b:
#             graph[a][b] = 0

# for i in range(M):
#     s, e, t = map(int, input().split())
#     graph[s][e] = t

# for k in range(1, N+1):
#     for a in range(1, N+1):
#         for b in range(1, N+1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# costs = [0] * (N+1)

# for i in range(1, N+1):
#     costs[i] = graph[i][X] + graph[X][i]

# print(max(costs))