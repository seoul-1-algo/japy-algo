import sys
sys.stdin = open('2096.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

min_val = [[0] * 3 for _ in range(2)]
max_val = [[0] * 3 for _ in range(2)]

min_val[0] = arr[0][:]
max_val[0] = arr[0][:]

for i in range(1, N):
    min_val[1][0] = arr[i][0] + min(min_val[0][0], min_val[0][1])
    max_val[1][0] = arr[i][0] + max(max_val[0][0], max_val[0][1])   

    min_val[1][1] = arr[i][1] + min(min_val[0][0], min_val[0][1], min_val[0][2])
    max_val[1][1] = arr[i][1] + max(max_val[0][0], max_val[0][1], max_val[0][2])

    min_val[1][2] = arr[i][2] + min(min_val[0][1], min_val[0][2])
    max_val[1][2] = arr[i][2] + max(max_val[0][1], max_val[0][2])

    min_val[0] = min_val[1][:]
    max_val[0] = max_val[1][:]

print(max(max_val[0]), min(min_val[0]))
