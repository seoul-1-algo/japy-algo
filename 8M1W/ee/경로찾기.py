import sys
sys.stdin = open('11403.txt')

from collections import deque

def bfs(start):
    visited = [0] * N
    queue = deque([start])

    while queue:
        node = queue.popleft()

        for next in graph[node]:
            if not visited[next]:
                queue.append(next)
                visited[next] = 1

    return visited

N = int(input()) # 정점의 개수

graph = [[] for _ in range(N)]

for i in range(N):
    row = list(map(int, input().split()))
    graph[i] = [j for j in range(N) if row[j] == 1] # 연결된 노드 추가

for i in range(N):
    result = bfs(i)
    print(*result)