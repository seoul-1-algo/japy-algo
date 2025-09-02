n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dp_max = [[0, 0, 0] for _ in range(n)]  # 최대값 dp
dp_min = [[10e6, 10e6, 10e6] for _ in range(n)]     # 최소값 dp

for i in range(n):
    if i == 0:
        dp_max[i] = graph[i]
        dp_min[i] = graph[i]
    else:
        dp_max[i][0] = graph[i][0] + max(dp_max[i - 1][0], dp_max[i - 1][1])
        dp_max[i][1] = graph[i][1] + max(dp_max[i - 1])
        dp_max[i][2] = graph[i][2] + max(dp_max[i - 1][1], dp_max[i - 1][2])

        dp_min[i][0] = graph[i][0] + min(dp_min[i - 1][0], dp_min[i - 1][1])
        dp_min[i][1] = graph[i][1] + min(dp_min[i - 1])
        dp_min[i][2] = graph[i][2] + min(dp_min[i - 1][1], dp_min[i - 1][2])

print(max(dp_max[-1]), min(dp_min[-1]))
