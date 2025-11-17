import sys
sys.stdin = open('11054.txt')

N = int(input())
arr = list(map(int, input().split()))

dp_asc = [1] * N

for i in range(N):

    for j in range(i):
        if arr[i] > arr[j]:
            dp_asc[i] = max(dp_asc[i], dp_asc[j] + 1)

dp_dsc = [1] * N

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if arr[i] > arr[j]:
            dp_dsc[i] = max(dp_dsc[i], dp_dsc[j] + 1)

# print(dp_asc)
# print(dp_dsc)

ans = 0
for i in range(N):
    ans = max(ans, dp_asc[i] + dp_dsc[i] - 1)

print(ans)