from heapq import heappop, heappush

n = int(input())
m = int(input())

edges = [list() for _ in range(n + 1)]
for _ in range(m):
    s, e, c = list(map(int, input().split()))
    edges[s].append([c, e])     # 비용, 목적지

start, end = list(map(int, input().split()))
heap = [[0, start]]
distance = [1e10 for _ in range(n + 1)]

while heap:
    dist, curr = heappop(heap)

    if distance[curr] < dist:
        continue
    distance[curr] = dist

    for cost, node in edges[curr]:
        if dist + cost < distance[node]:
            distance[node] = dist + cost
            heappush(heap, [dist + cost, node])

print(distance[end])
