import sys
sys.stdin = open('1197.txt')

v, e = map(int, input().split()) # 정점의 개수 v, 간선의 개수 e

# 각 간선에 대한 정보
edges = []

for _ in range(e):
    a, b, c = map(int, input().split()) 
    edges.append((c, a, b))

edges.sort() # 비용이 작은 순으로 정렬

# 부모 테이블
parent = [i for i in range(v + 1)] # 자기 자신으로 초기화


# Union-Find 알고리즘
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x]) # 루트 노드를 찾을 때까지 재귀적으로 호출
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root < y_root:
        parent[y_root] = x_root
    else:
        parent[x_root] = y_root


# 최소 스패닝 트리 구하는 크루스칼 알고리즘
result = 0 # 가중치의 합

for c, a, b in edges:
    # 사이클 생성 안 하면 선택!
    if find(a) != find(b): # 두 정점이 같은 최상위 parent를 갖지 않으면 사이클 아님
        union(a, b)
        result += c

print(result)