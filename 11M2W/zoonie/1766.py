import sys
import heapq

input = sys.stdin.readline

n,m = map(int,input().split())
ans = []
graph = [[] for i in range(n+1)]
degree = [0 for i in range(n+1)]
queue = []

for i in range(m):
    pre, next = map(int,input().split())
    graph[pre].append(next)
    degree[next]+=1

for i in range(1,n+1):
    if degree[i] == 0:
        heapq.heappush(queue,i)
    

while queue:
    now = heapq.heappop(queue)
    ans.append(now)
    for i in graph[now]:
        degree[i]-=1
        if degree[i]==0:
            heapq.heappush(queue,i)

print(" ".join(map(str,ans)))