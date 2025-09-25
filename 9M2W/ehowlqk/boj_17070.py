n = int(input())

house = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1

for i in range(n):
    for j in range(1, n):
        if house[i][j]:
            continue

        hor, diag, vert = dp[i][j]

        # i + 1
        if i < n - 1 and house[i + 1][j] == 0:
            dp[i + 1][j][2] += diag + vert  # 아래로 이동
            # i + 1 && j + 1
            if j < n - 1 and house[i][j + 1] == 0 and house[i + 1][j + 1] == 0:
                dp[i + 1][j + 1][1] += hor + diag + vert     # 대각선 이동

        if j < n - 1 and house[i][j + 1] == 0:
            dp[i][j + 1][0] += hor + diag    # 옆으로 이동

print(sum(dp[-1][-1]))