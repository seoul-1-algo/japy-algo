import sys
sys.stdin = open('2166.txt')

N = int(input())
ans = 0

point = [list(map(int, input().split())) for _ in range(N)] # 다각형의 점들
point.insert(0, [])

for i in range(1, N+1):
    if i == N:
        ans += point[i][0] * point[1][1]
        ans -= point[1][0] * point[i][1]
    else:
        ans += point[i][0] * point[i+1][1]
        ans -= point[i+1][0] * point[i][1]

print(abs(ans)/2)