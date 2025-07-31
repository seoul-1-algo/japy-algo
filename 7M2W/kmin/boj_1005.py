import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    d = list(map(int, input().split()))
    xy = [[] for _ in range(N + 1)]     # 간선정
    indgree = [0 for _ in range(N + 1)] # 건물을 짓기 전에 지어야 하는 건물의 수
    dp = [0 for _ in range(N + 1)]  # 해당 인덱스 건물 짓는 최소 시간
    queue = deque()

    for _ in range(K):
        x, y = map(int, (input().split()))
        xy[x].append(y)
        indgree[y] += 1 # y 진입차수 증가


    W = int(input())

    for i in range(1, N + 1):
        if indgree[i] == 0:     # 선행 조건이 없으면
            queue.append(i)
            dp[i] = d[i - 1]    # 자기 건설 시작
    
    while queue:
        now = queue.popleft()   # g현재 짓고 있는 건물

        for i in xy[now]:   # now를 지은 후 지을 수 있는 건물들
            indgree[i] -= 1     # 선행 조건 하나 해제
            # dp[i]는 지금까지 계산된 최소 시간 vs tmp 거쳐서 짓는 시간
            dp[i] = max(dp[i], dp[now] + d[i - 1])  # dp[now] : 현재 건물이 짔는데까지 걸린 누적 시간, dp[i - 1] : i번 건물 자체를 짓는데 걸린 시간
            if indgree[i] == 0: # 더이상 기다릴 필요 X
                queue.append(i)

    print(dp[W])