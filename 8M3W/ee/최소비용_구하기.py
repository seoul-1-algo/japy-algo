import sys
sys.stdin = open('1916.txt')

import heapq

INF = 1e6

n = int(input()) # 도시의 수
m = int(input()) # 버스의 수

graph = [[] for _ in range(n+1)] # 버스 정보를 저장할 인접 리스트
distance = [INF] * (n+1) # 최단 거리를 저장할 리스트

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

s, e = map(int, input().split()) # 출발 도시, 도착 도시

def dijkstra(start, end):
    queue = []

    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for next, weight in graph[now]:
            cost = dist + weight

            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(queue, (cost, next))
                
    return distance[end]

print(dijkstra(s, e))