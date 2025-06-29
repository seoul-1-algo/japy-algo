import heapq

n, m = map(int, input().split())

ladders, snakes = dict(), dict()

for _ in range(n):
    start, end = map(int, input().split())
    ladders[start] = end

for _ in range(m):
    start, end = map(int, input().split())
    snakes[start] = end

# 간선 작업
edges = [[] for _ in range(101)]
for i in range(1, 100):
    for j in range(1, 7):
        if i + j in ladders:
            edges[i].append(ladders[i + j])
        elif i + j in snakes:
            edges[i].append(snakes[i + j])
        elif i + j <= 100:
            edges[i].append(i + j)

# 다익스트라로 최단경로 찾기
dist = [1e9] * 101
dist[1] = 0


def dijkstra():
    heap = [[-1, 0]]
    while heap:
        node, cost = heapq.heappop(heap)
        if dist[-1 * node] < cost:
            continue

        for endNode in edges[-1 * node]:
            if cost + 1 < dist[endNode]:
                dist[endNode] = cost + 1
                heapq.heappush(heap, [-1 * endNode, cost + 1])


dijkstra()
print(dist[100])
