import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
dp = [[0]*N for i in range(N)]
M = int(input())
for i in range(N):  # 길이가 1이면 무조건 팰린드롬
    dp[i][i] = 1

for i in range(N - 1):      # 길이가 2이면, 두 숫자 비교해서 같으면 팰린드롬, 아니면 아님
    if arr[i] == arr[i + 1]:
        dp[i][i + 1] = 1
    else:
        dp[i][i + 1] = 0

for cnt in range(3, N + 1): # 길이가 3이상이면
    for i in range(N - cnt + 1):
        j = i + cnt - 1
        if arr[i] == arr[j] and dp[i + 1][j - 1] == 1:  # 시작과 끝이 같고, 그 사이 dp 값이 1이면
            dp[i][j] = 1    # dp[i][j]는 팰린드롬이다


for i in range(M):
    S, E = map(int, input().split())
    print(dp[S - 1][E - 1])
    