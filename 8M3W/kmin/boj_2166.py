import sys
input = sys.stdin.readline
# answer = 1/2 * |x1y2-x2y1 + x2y3-x3y2 + ..... + xny1-x1yn|
N = int(input())
arr = []    # 꼭짓점 좌표
for _ in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])
arr.append(arr[0])  # 첫 꼭짓점을 마지막에 한번 더 추가

answer = 0
for i in range(N):
    x1, y1 = arr[i]
    x2, y2 = arr[i + 1]
    answer += x1 * y2 - x2 * y1

print(round(abs(answer)/2, 1))