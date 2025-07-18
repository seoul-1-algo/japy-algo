import sys

sys.stdin = open('1005.txt')

from collections import deque

T = int(input()) # 테스트케이스 개수

for _ in range(T):
    N, K = map(int, input().split()) # N: 건물의 개수, K: 건설순서 규칙의 총 개수

    D = [0] + list(map(int, input().split())) # 각 건물당 건설에 걸리는 시간

    graph = [[] for _ in range(N+1)]
    level = [0] * (N+1) # 위상 정렬에서 사용하는 차수 ?

    for __ in range(K):
        x, y = map(int, input().split())
        graph[x].append(y)
        level[y] += 1

    # print(graph)
    
    W = int(input()) # 백준이가 승리하기 위해 건설해야 할 건물의 번호

    q = deque()
    result = [0] * (N+1)

    for i in range(1, N+1):
        if level[i] == 0:
            q.append((i, D[i]))
            result[i] = D[i]

    while q:
        now, time = q.popleft()
        
        for next in graph[now]:
            level[next] -= 1

            cal_time = time + D[next]

            if result[next] < cal_time:
                result[next] = cal_time

            if level[next] == 0:
                q.append((next, result[next]))

    print(result[W])