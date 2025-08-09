from collections import deque

# 입력
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 결과 행렬 초기화 (모두 0)
result = [[0] * N for _ in range(N)]

# 각 정점 i에 대해 BFS 수행
for i in range(N):
    visited = [False] * N
    queue = deque()

    # i에서 직접 도달 가능한 정점들을 먼저 큐에 넣음
    for j in range(N):
        if matrix[i][j] == 1:
            queue.append(j)
            visited[j] = True

    # BFS 수행
    while queue:
        cur = queue.popleft()
        result[i][cur] = 1

        for next_node in range(N):
            if matrix[cur][next_node] == 1 and not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

# 출력
for row in result:
    print(*row)
