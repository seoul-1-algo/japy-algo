import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
# 친구관계
graph = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 1번부터 케빈베이컨 수
ans = []
for i in range(1, N + 1):   # 1부터 N까지 bfs
    visited = [0] * (N + 1)
    queue = deque([i])
    visited[i] = 1  # 1부터 시작하니 마지막에 -1 해줘야 함, 방문 여부 + 케빈 베이컨 수 까지 계산해야해서 1로
    while queue:
        x = queue.popleft()
        for j in graph[x]:  # x의 친구들 들 순회
            if not visited[j]:
                visited[j] = visited[x] + 1 # j는 이전 사람 + 1
                queue.append(j)
    ans.append(sum(visited) - N)    # visted에서 1부터 시작하므로

fin = ans.index(min(ans)) + 1
print(fin)
