from collections import deque

# input = open('2623.txt', 'r').readline
n, m = map(int, input().split())

indegrees = [0 for _ in range(n+1)]
edges = [[] for _ in range(n+1)]

bc = list()
for _ in range(m):
    tmp = list(map(int, input().split()))
    for i in range(1, len(tmp) - 1):
        indegrees[tmp[i+1]] += 1
        edges[tmp[i]].append(tmp[i+1])

def solution(indegrees, edges):
    result = []
    q = deque([])
    for singer in range(1, n+1):
        if indegrees[singer] == 0:
            q.append(singer)

    while q:
        singer = q.popleft()
        result.append(singer)
        for nxt in edges[singer]:
            # 사이클 형성되는 경우 0 출력
            if indegrees[nxt] == 0:
                return [0]
            indegrees[nxt] -= 1
            if indegrees[nxt] == 0:
                q.append(nxt)
    
    # 모든 간선이 연결되지 않아 순서를 이루지 못하는 경우 0 출력
    if len(result) < len(edges) - 1:
        return [0]

    return result


answer = solution(indegrees, edges)
for singer in answer:
    print(singer)
    