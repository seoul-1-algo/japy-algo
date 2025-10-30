first  = input().rstrip()
second = input().rstrip()

if not first or not second:     # 둘 중 하나가 비어 있으면
    print(0)
    print("")
    exit()

n, m = len(first), len(second)
dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if first[i-1] == second[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# LCS 문자열 복원
i, j = n, m
lcs = []
while i > 0 and j > 0:
    if first[i-1] == second[j-1]:
        lcs.append(first[i-1])
        i -= 1
        j -= 1
    elif dp[i-1][j] >= dp[i][j-1]:
        i -= 1
    else:
        j -= 1

lcs.reverse()
print(dp[n][m])
print("".join(lcs))
