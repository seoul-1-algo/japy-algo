import sys
sys.stdin = open('10282.txt')

import heapq

T = int(input()) # 테스트 케이스 수
INF = int(1e9)

def dijkstra(start, graph, n):
    q = []
   
    heapq.heappush(q, (0, start)) # (걸린 시간, 노드)
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next in graph[now]: # now에서 next로 전파
            cost = dist + next[1] # next가 감염되는 데 걸리는 시간

            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))

    # 감염되는 컴퓨터 수, 마지막 컴퓨터가 감염되기까지 걸리는 시간
    cnt, time = 0, 0

    for d in distance:
        if d != INF: # 감염됐으면
            cnt += 1
            time = max(time, d) # 가장 늦게 감염된 시간 갱신
    
    print(cnt, time)

for _ in range(T):
    n, d, c = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1) # distance[i] : c에서 i 컴퓨터가 감염되는 데 걸리는 최소 시간

    for __ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    
    dijkstra(c, graph, n)