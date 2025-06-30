# 이중 우선순위 큐
import sys
import heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    min_h = []
    max_h = []
    visited = [False] * k

    for i in range(k):
        cmd, num = input().split()
        num = int(num)

        if cmd == 'I':
            heapq.heappush(min_h, (num, i))
            heapq.heappush(max_h, (-num, i))
            visited[i] = True
        else:
            if num == 1:
                # 최대값 제거
                while max_h and not visited[max_h[0][1]]:
                    heapq.heappop(max_h)
                if max_h:
                    visited[max_h[0][1]] = False
                    heapq.heappop(max_h)
            else:
                # 최소값 제거
                while min_h and not visited[min_h[0][1]]:
                    heapq.heappop(min_h)
                if min_h:
                    visited[min_h[0][1]] = False
                    heapq.heappop(min_h)

    # 마지막 정리: 유효하지 않은 값 제거
    while min_h and not visited[min_h[0][1]]:
        heapq.heappop(min_h)
    while max_h and not visited[max_h[0][1]]:
        heapq.heappop(max_h)

    if not min_h or not max_h:
        print("EMPTY")
    else:
        print(-max_h[0][0], min_h[0][0])
