import sys
sys.stdin = open('12014.txt')

T = int(input()) 

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    dp = [1] * N
    answer = 0

    for i in range(N):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

        if dp[i] >= K:
            answer = 1
            break

    print(f'Case #{tc}')
    print(answer)