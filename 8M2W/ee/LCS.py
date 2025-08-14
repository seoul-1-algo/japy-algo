import sys
sys.stdin = open('9251.txt')

string_1 = list(input())
string_2 = list(input())

dp = [[0] * (len(string_1) + 1) for _ in range(len(string_2) + 1)]

for i in range(1, len(string_2) + 1):
    for j in range(1, len(string_1) + 1):
        if string_2[i - 1] == string_1[j - 1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(string_2)][len(string_1)])