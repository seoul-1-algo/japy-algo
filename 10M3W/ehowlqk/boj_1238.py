from heapq import heappush, heappop
MAX_DIST = 100000

def dijkstra(start, end):
    hq = []
    heappush(hq, (0, start))
    distances = [MAX_DIST]*(n+1)
    distances[start] = 0
    
    while hq:
        dist, node = heappop(hq)
        
        if dist > distances[node]:
            continue

        for cost, next in roads[node]:
            if dist + cost < distances[next]:
                distances[next] = dist + cost
                heappush(hq, (dist + cost, next))
                
    return distances[end]


n, m, x = map(int, input().split())

roads = [list() for _ in range(n+1)]
for _ in range(m):
    s, e, t = map(int, input().split())
    roads[s].append((t, e))

max_time = 0

for i in range(1, n+1):
    i_time = dijkstra(i, x) + dijkstra(x, i)
    max_time = max(i_time, max_time)

print(max_time)
