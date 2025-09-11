n = int(input())
dp_max = [0, 0, 0]  # 최대값 dp
dp_min = [10e6, 10e6, 10e6]     # 최소값 dp


for i in range(n):
    row = list(map(int, input().split()))
    if i == 0:
        dp_max, dp_min = row, row
    else:
        dp_max = [row[0] + max(dp_max[0], dp_max[1]), row[1] + max(dp_max), row[2] + max(dp_max[1], dp_max[2])]
        dp_min = [row[0] + min(dp_min[0], dp_min[1]), row[1] + min(dp_min), row[2] + min(dp_min[1], dp_min[2])]

print(max(dp_max), min(dp_min))
