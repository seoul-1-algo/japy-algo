from heapq import heappop, heappush
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())    
    edges[a].append((c, b))
    edges[b].append((c, a))

hq = [(0, 1)]
visited = [False] * (n + 1)
n_span = 0
uzb, max_uzb = 0, 0

while hq:
    dist, node = heappop(hq)

    if visited[node]:
        continue
    visited[node] = True
    
    n_span += 1
    uzb += dist
    max_uzb = max(max_uzb, dist)
    
    # MST 완성되기 바로 전 단계 -> 마을이 두개로 쪼개진 상태
    if n_span == n:
        break

    for cost, next in edges[node]:
        heappush(hq, (cost, next))

print(uzb - max_uzb)
