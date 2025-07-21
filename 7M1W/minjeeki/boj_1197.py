# 최소 스패닝 트리
# v : 정점 / e : 간선
v, e = map(int, input().split())
# owners : 대표 배열 (초기화 자기자신
owners = [i for i in range(v + 1)]
# connection : 연결 관계 (가중치 기준 오름차순) / 정렬 진행했기에 순차 조회 시 가장 작은 가중치가 먼저 계산됨
connections = [tuple(map(int, input().split())) for _ in range(e)]
connections.sort(key=lambda x: x[2])
# 최소 가중치로 연결된 트리(최소 스패닝 트리)의 가중치
total = 0

# find 함수 : 최상위 대표 찾기 (이전에 합친 적 있다면 진짜 대표 찾기)
def find(x):
    while owners[x] != x:
        owners[x] = owners[owners[x]]  # 경로 압축
        x = owners[x]
    return x

# union 함수 : 트리에 포함되지 않은 정점을 트리로 병합시키는 과정
def union(a, b):
    a_owner = find(a)
    b_owner = find(b)
    # 대표 다름 + 연결 관계 -> 둘 중 작은 값을 대표로 병합 -> 연결 성공 표시
    if a_owner != b_owner:
        if a_owner < b_owner:
            owners[b_owner] = a_owner
        else:
            owners[a_owner] = b_owner
        return True
    # 대표 동일 : 사이클을 가짐
    return False

# a, b : 정점 / c : 가중치
for a, b, c in connections:
    # 트리에 포함되지 않았던 정점이 병합됐다면, MST에 포함
    if union(a, b):
        total += c

print(total)
