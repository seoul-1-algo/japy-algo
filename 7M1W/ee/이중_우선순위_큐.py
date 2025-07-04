import sys
sys.stdin = open('7662.txt')

import heapq

T = int(input()) # 입력 데이터의 수

for _ in range(T):
    k = int(input()) # Q에 적용할 연산의 개수

    min_heap = [] # 최소 힙
    max_heap = [] # 최대 힙

    cnt = dict() # 힙에 들어있는 원소의 개수를 셀 딕셔너리
    
    for __ in range(k):
        op, val = input().split()
        val = int(val)

        if op == 'I': # 삽입 연산
            heapq.heappush(min_heap, val) # 최소 힙에 추가
            heapq.heappush(max_heap, -val) # 최대 힙에 추가

            cnt[val] = cnt.get(val, 0) + 1

        elif val == 1: # 최댓값 삭제
            while max_heap:
                n = -heapq.heappop(max_heap)
                if cnt.get(n, 0) > 0: # 아직 힙에 남아 있다면
                    cnt[n] -= 1
                    break

        else: # 최솟값 삭제
            while min_heap:
                n = heapq.heappop(min_heap)
                if cnt.get(n, 0) > 0:
                    cnt[n] -= 1
                    break

        # print("최소 힙: ", min_heap)
        # print("최대 힙: ", max_heap)

    max_val = None
    min_val = None

    while max_heap:
        n = - heapq.heappop(max_heap)
        if cnt.get(n, 0) > 0:
            max_val = n
            break

    while min_heap:
        n = heapq.heappop(min_heap)
        if cnt.get(n, 0) > 0:
            min_val = n
            break

    if max_val is not None and min_val is not None:
        print(max_val, min_val)
    else:
        print('EMPTY')
    