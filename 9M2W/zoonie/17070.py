import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

board = []

for i in range(n):
    board.append(list(map(int,input().split())))
      
dp = [[[0,0,0] for i in range(n)] for i in range(n)]

dp[0][1][0] = 1  # 시작 위치: (0,1) 가로 방향

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            continue

        # 가로에서 가로 or 대각선
        if j-1 >= 0:
            dp[i][j][0] += dp[i][j-1][0] + dp[i][j-1][2]
        
        # 세로에서 세로 or 대각선
        if i-1 >= 0:
            dp[i][j][1] += dp[i-1][j][1] + dp[i-1][j][2]
        
        # 대각선에서 가로, 세로, 대각선
        if i-1 >= 0 and j-1 >= 0:
            if board[i-1][j] == 0 and board[i][j-1] == 0:
                dp[i][j][2] += dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

print(sum(dp[n-1][n-1]))