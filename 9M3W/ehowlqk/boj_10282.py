from heapq import heappop, heappush
import sys

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    n, d, c = map(int, input().split())
    dependencies = [list() for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        dependencies[b].append((s, a))

    hq = [(0, c)]
    visited = [False] * (n + 1)
    answer = 0
    while hq:
        time, infected = heappop(hq)

        if visited[infected]:
            continue
        visited[infected] = True
        answer = max(answer, time)

        for s, a in dependencies[infected]:
            if not visited[a]:
                heappush(hq, (time + s, a))

    print(sum(visited), answer)
