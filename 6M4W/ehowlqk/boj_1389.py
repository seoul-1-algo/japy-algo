n, m = map(int, input().split())

# 거리 배열 초기화
distances = [[0 if row == col else 1e9 for col in range(n)] for row in range(n)]

# 노드 사이 거리 입력
for _ in range(m):
    a, b = map(int, input().split())
    distances[a-1][b-1] = 1
    distances[b-1][a-1] = 1

# 노드 간 거리 업데이트
for k in range(n):
    for i in range(n):
        for j in range(n):
            distances[i][j] = min(distances[i][k] + distances[k][j], distances[i][j])

answer = 0
minKevinBacon = 1e9

# 케빈 베이컨 가장 작은 유저 구하기
for user in range(1, n+1):
    kevinBacon = sum(distances[user - 1])
    if kevinBacon < minKevinBacon:
        minKevinBacon = kevinBacon
        answer = user

print(answer)
