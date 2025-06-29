import sys
from heapq import heappop, heappush

tc = int(input())

for _ in range(tc):
    k = int(input())

    max_heap = list()   # 최대힙(음수로 저장)
    min_heap = list()   # 최소힙
    nums_cnt = dict()   # value: 전체 우선순위 큐에서 key의 개수

    for __ in range(k):
        task, num = sys.stdin.readline().split()
        num = int(num)
        if task == "I":
            heappush(max_heap, -num)    # 최대 힙 추가
            heappush(min_heap, num)     # 최소 힙 추가
            nums_cnt[num] = nums_cnt.get(num, 0) + 1    # 개수 추가

        elif task == "D" and len(nums_cnt):
            # 최대 값 삭제
            if num == 1:
                # 최소값 삭제 시 최대 힙에서 반영되지 않은 삭제 진행
                while -max_heap[0] not in nums_cnt:
                    heappop(max_heap)
                val = -heappop(max_heap)
                # dict에서 삭제 처리
                nums_cnt[val] -= 1
                if nums_cnt[val] == 0:
                    del nums_cnt[val]

            # 최소값 pop
            elif num == -1:
                while min_heap[0] not in nums_cnt:
                    heappop(min_heap)
                val = heappop(min_heap)
                # dict에서 삭제 처리
                nums_cnt[val] -= 1
                if nums_cnt[val] == 0:
                    del nums_cnt[val]

    while max_heap and -max_heap[0] not in nums_cnt:
        heappop(max_heap)
    while min_heap and min_heap[0] not in nums_cnt:
        heappop(min_heap)
    if nums_cnt.items():
        print(-max_heap[0], min_heap[0])
    else:
        print("EMPTY")
