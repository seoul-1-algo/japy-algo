from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    times = list(map(int, input().split()))
    edges = [list() for _ in range(N + 1)]
    for _ in range(K):
        X, Y = map(int, input().split())
        edges[Y].append(X)

    W = int(input())

    q = deque([(W, times[W - 1])])
    visited = [0] * (N + 1)
    visited[W] = times[W - 1]

    while q:
        node, time = q.popleft()

        if time < visited[node]:
            continue

        for prev in edges[node]:
            if visited[prev] < visited[node] + times[prev - 1]:
                visited[prev] = visited[node] + times[prev - 1]
                q.append((prev, visited[prev]))

    print(max(visited))
