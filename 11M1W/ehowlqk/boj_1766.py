from heapq import heappop, heappush
import sys

input = sys.stdin.readline
# input = open('boj_1766.txt', 'r').readline

n, m = map(int, input().split())

edges = [[] for x in range(n + 1)]      # 간선 정보
indegree = [0 for x in range(n+1)]      # 진입차수

hq = []

for _ in range(m):
    prev, nxt = map(int, input().split())
    edges[prev].append(nxt)
    indegree[nxt] += 1

for problem in range(1, n + 1):
    if indegree[problem] == 0:
        heappush(hq, problem)

while hq:
    problem = heappop(hq)
    print(problem, end=' ')
    for nxt in edges[problem]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heappush(hq, nxt)
