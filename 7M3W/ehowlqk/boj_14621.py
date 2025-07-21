import sys
input = sys.stdin.readline


def union(u, v):
    root_u, root_v = find(u), find(v)
    if root_u != root_v:
        parents[root_v] = root_u


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    
    return parents[x]


n, m = map(int, input().split())
gender = input().split()

routes = []
for _ in range(m):
    routes.append(list(map(int, input().split())))
routes.sort(key=lambda x: x[2])

parents = [i for i in range(n)]
answer = 0
cnt = 0

for route in routes:
    u, v, d = route
    if gender[u-1] != gender[v-1] and find(u-1) != find(v-1):
        union(u-1, v-1)
        answer += d
        cnt += 1

print(answer if cnt == n - 1 else -1)
