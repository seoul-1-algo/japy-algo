from sys import stdin

N = int(input())
arr = list(map(int, stdin.readline().split()))
maxDP = arr # 첫 행 기준 최댓 DP (주의: 이 시점엔 arr와 같은 리스트를 가리킴)
minDP = arr
for _ in range(N - 1):
    arr = list(map(int, stdin.readline().split()))
    # 최댓값 DP 갱신
    # maxDP[0] <- arr[0] + max(이전 maxDP[0], 이전 maxDP[1])
    # maxDP[1] <- arr[1] + max(이전 maxDP[0], 이전 maxDP[1], 이전 maxDP[2])
    # maxDP[2] <- arr[2] + max(이전 maxDP[1], 이전 maxDP[2])
    maxDP = [arr[0] + max(maxDP[0], maxDP[1]), arr[1] + max(maxDP), arr[2] + max(maxDP[1], maxDP[2])]
    
    # 최솟값 DP 갱신 (최댓값 로직에서 max → min만 바뀜)
    # minDP[0] <- arr[0] + min(이전 minDP[0], 이전 minDP[1])
    # minDP[1] <- arr[1] + min(이전 minDP[0], 이전 minDP[1], 이전 minDP[2])
    # minDP[2] <- arr[2] + min(이전 minDP[1], 이전 minDP[2])
    minDP = [arr[0] + min(minDP[0], minDP[1]), arr[1] + min(minDP), arr[2] + min(minDP[1], minDP[2])]

print(max(maxDP), min(minDP))