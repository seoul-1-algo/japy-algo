from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

# 방향과 순서에 대한 정보 입력
for _ in range(M):
    sequence = list(map(int, input().split()))
    singer_count = sequence[0]
    for i in range(1, singer_count):
        graph[sequence[i]].append(sequence[i + 1])
        indegree[sequence[i + 1]] += 1

# 진입차수가 0(의존성 없음)인 노드를 큐에 추가
queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

# 다음 순서의 노드를 큐에 넣으면서 진입차수를 줄임
result = []
while queue:
    current = queue.popleft()
    result.append(current)
    for next in graph[current]:
        indegree[next] -= 1
        # 진입차수가 0이 되면 큐에 추가
        if indegree[next] == 0:
            queue.append(next)

# 결과 출력 (모든 노드를 방문했다면 순서대로 출력, 아니면 0 출력)
if len(result) == N:
    print(*result)
else:
    print(0)
