import sys
sys.stdin = open('2623.txt')

from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split()) # N: 가수의 수, M: 보조 PD의 수
arr = [list(map(int, input().split())) for _ in range(M)]

indeg = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for i in range(M):
    k = arr[i][0] # 담당 가수 수

    for j in range(1, k):
        A = arr[i][j]
        B = arr[i][j+1]

        graph[A].append(B)
        indeg[B] += 1

q = deque()
for node in range(1, N+1):
    if indeg[node] == 0:
        q.append(node)

ans = []
while q:
    node = q.popleft()
    ans.append(node)

    for nxt in graph[node]:
        indeg[nxt] -= 1
        if indeg[nxt] == 0:
            q.append(nxt)

if len(ans) != N:
    print(0)
else:
    for val in ans:
        print(val)