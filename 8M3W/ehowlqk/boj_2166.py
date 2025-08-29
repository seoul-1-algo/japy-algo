n = int(input())
coors = [list(map(int, input().split())) for _ in range(n)]

cross_sum = 0
for i in range(n):
    x1, y1 = coors[i-1]
    x2, y2 = coors[i]
    print(x1*y2 - x2*y1)
    cross_sum += x1*y2 - x2*y1

print(round(abs(cross_sum)/2, 2))