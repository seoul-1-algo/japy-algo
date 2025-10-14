from collections import deque

dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
LEN_DIR = len(dir)

# 0. 초기 세팅 : 입력값 처리 + cheese 전체 개수 확인
N, M = map(int, input().split())
num_cheese = 0
answer_time = 0
matrix = [[] for _ in range(N)]
for idx in range(N):
    matrix[idx] = list(map(int, input().split()))
    num_cheese += sum(matrix[idx])

# 0. 초기 세팅 : 초기 외부 공기 표시 (0 -> -1 값 갱신)
queue = deque()
for j in range(M):
    if matrix[0][j] == 0:
        queue.append((0, j))
        matrix[0][j] = -1
    if matrix[N-1][j] == 0:
        queue.append((N-1, j))
        matrix[N-1][j] = -1
for i in range(N):
    if matrix[i][0] == 0:
        queue.append((i, 0))
        matrix[i][0] = -1
    if matrix[i][M-1] == 0:
        queue.append((i, M-1))
        matrix[i][M-1] = -1
while queue:
    r, c = queue.popleft()
    for dr, dc in dir:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and matrix[nr][nc] == 0:
            matrix[nr][nc] = -1
            queue.append((nr, nc))

# 1. 치즈 녹이기 반복
while num_cheese > 0:
    # 1-1. 녹을 치즈 찾기 (외부 공기에 2면 이상 접촉)
    to_melt = []
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                air_count = 0
                for dr, dc in dir:
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < N and 0 <= nc < M and matrix[nr][nc] == -1:
                        air_count += 1
                if air_count >= 2:
                    to_melt.append((i, j))
    
    # 1-2. 치즈 녹이기 & 녹은 치즈 주변 0 존재 시 DFS 활용 -> -1 변환
    for r, c in to_melt:
        matrix[r][c] = -1
        num_cheese -= 1
        
        queue = deque([(r, c)])
        while queue:
            cr, cc = queue.popleft()
            for dr, dc in dir:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < N and 0 <= nc < M and matrix[nr][nc] == 0:
                    matrix[nr][nc] = -1
                    queue.append((nr, nc))
    
    answer_time += 1

print(answer_time)