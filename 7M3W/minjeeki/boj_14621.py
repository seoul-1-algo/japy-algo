def find(x):
    if owner[x] != x:
        owner[x] = find(owner[x])
    return owner[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        owner[root_y] = root_x
        return True
    return False

n, m = map(int, input().split())
gender = [''] + input().split()
expected_connection = n - 1

lines = []
for _ in range(m):
    u, v, cost = map(int, input().split())
    if gender[u] != gender[v]:
        lines.append((cost, u, v))

lines.sort()
owner = list(range(n + 1))

total_cost = 0
connection_cnt = 0

for cost, u, v in lines:
    if union(u, v):
        total_cost += cost
        connection_cnt += 1

if connection_cnt == expected_connection:
    print(total_cost)
else:
    print(-1)
