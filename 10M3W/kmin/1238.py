import sys
input = sys.stdin.readline
inf = int(1e9)
N, M , X = map(int, input().split())    # N : 학생 수 , M : 도로 개수, X : 파티가 열리는 마을 번호
arr = [[inf] * (N+1) for _ in range(N+1)]   # 초기에는 모든 거리 무한대로 설정
for i in range(1, N + 1):   # 자기 자신으로 가는 거리 0
    for j in range(1, N + 1):
        if i == j:
            arr[i][j] = 0
# 단방향 도로 입력
for _ in range(M):
    start, end , time = map(int, input().split())
    arr[start][end] = time  # 출발지에서 도착지로 가는데 걸리는 시간

for k in range(1, N + 1):
    for i in range(1, N + 1):   # 출발 노드
        for j in range(1, N + 1):   #도착 노드
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

answer = 0
for i in range(1, N + 1):
    answer = max(answer, arr[i][X] + arr[X][i])  # i>x, x->i 가는데 걸리는 시

print(answer)