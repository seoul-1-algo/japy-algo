import sys
input = sys.stdin.readline
N, M = map(int, input().split())
gender = list(input().split())
uvds = []
for _ in range(M):
    u, v, d = map(int, input().split())
    uvds.append((d, v, u))  # 거리 기준 정렬하려고
uvds.sort()
answer = 0  # 답
check = 0   # 간선 수

def find_parent(x): # 파인드 함수
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b): # 유니온 함순
    a = find_parent(a)
    b = find_parent(b)
    if a < b:   # 더 작은 번호를 부모로
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(N + 1)]

for uvd in uvds:
    distance, a, b = uvd
    if find_parent(a) != find_parent(b) and gender[a - 1] != gender[b - 1]: # 두 학교가 연결 X & 성별이 다름
        union_parent(a, b)
        answer += distance
        check += 1

if check == N - 1:  # mst 완성 되면
    print(answer)
else:
    print(-1)