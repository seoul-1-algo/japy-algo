from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    friends = list(map(int, input().split()))
    graph[friends[0]].append(friends[1])
    graph[friends[1]].append(friends[0])

def bfs(start):
    queue = deque([start])
    visited = [-1] * (N + 1)  # 모든 노드를 방문하지 않은 상태로 초기화 (-1)
    visited[start] = 0  # 시작 노드는 거리가 0

    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            if visited[neighbor] == -1:  # 방문하지 않은 노드인 경우
                visited[neighbor] = visited[current] + 1
                queue.append(neighbor)
    
    return sum(visited[1:])  # 각 노드의 거리를 합산해서 반환

kevin = [0] * (N + 1)

for i in range(1, N + 1):
    kevin[i] = bfs(i)

min_index = 1

for i in range(2, N + 1):
    if kevin[i] < kevin[min_index]:
        min_index = i

print(min_index)
