import sys
sys.stdin = open('17070.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp_hor = [[0] * N for _ in range(N)] # 가로 방향
dp_ver = [[0] * N for _ in range(N)] # 세로 방향
dp_dia = [[0] * N for _ in range(N)] # 대각선 방향

dp_hor[0][1] = 1

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            continue

        # 가로
        if j> 0:
            dp_hor[i][j] += dp_hor[i][j-1] + dp_dia[i][j-1]

        # 세로    
        if i > 0:
            dp_ver[i][j] += dp_ver[i-1][j] + dp_dia[i-1][j]
        
        # 대각
        if i>0 and j >0:
            if arr[i-1][j] == 0 and arr[i][j-1] == 0:
                dp_dia[i][j] += dp_hor[i-1][j-1] + dp_ver[i-1][j-1] + dp_dia[i-1][j-1]

print(dp_dia[N-1][N-1] + dp_hor[N-1][N-1] + dp_ver[N-1][N-1])