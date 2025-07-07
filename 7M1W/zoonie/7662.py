import sys
import heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    max_heap = []
    min_heap = []
    is_in_queue = {}
    length = 0
    for i in range(k):
        letter, num = map(str, input().split())
        num = int(num)

        if letter == 'I':
            heapq.heappush(max_heap,-num)
            heapq.heappush(min_heap,num)
            if num in is_in_queue:
                is_in_queue[num] += 1
            else:
                is_in_queue[num] = 1
            length += 1
        
        if letter == 'D':
            if length == 0:
                continue
            if num == -1:
                while True:
                    a = heapq.heappop(min_heap) 
                    if is_in_queue.get(a,0) >= 1:
                        is_in_queue[a] -= 1
                        break
                length-=1
            if num == 1:
                while True:
                    a = -heapq.heappop(max_heap)
                    if is_in_queue.get(a,0) >= 1:
                        is_in_queue[a]-=1
                        break
                length-=1

        while max_heap and is_in_queue.get(-max_heap[0],0) == 0:
            heapq.heappop(max_heap)
        while min_heap and is_in_queue.get(min_heap[0],0)==0:
            heapq.heappop(min_heap)

    if not max_heap or not min_heap:
        print('EMPTY')
    
    elif not max_heap:
        print(heapq.heappop(min_heap),heapq.heappop(min_heap))
    
    elif not min_heap:
        print(-heapq.heappop(max_heap),-heapq.heappop(max_heap))
    
    else:
        print(-heapq.heappop(max_heap), heapq.heappop(min_heap))
