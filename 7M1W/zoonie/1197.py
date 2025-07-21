import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
v, e = map(int, input().split())

edges = []
for _ in range(e):
    A, B, C = map(int, input().split())
    edges.append([A, B, C])

edges.sort(key=lambda x: x[2])

parent = [i for i in range(v + 1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

ans = 0
for a, b, cost in edges:
    if find_parent(a) != find_parent(b):
        ans += cost
        union(a, b)

print(ans)