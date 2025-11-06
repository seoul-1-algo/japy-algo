import sys
sys.stdin = open('2473.txt')

input = sys.stdin.readline

N = int(input())
liquids = list(map(int, input().split()))

liquids.sort() # 오름차순 정렬

min_sum = float('inf')
ans = []

for idx in range(N-2):
    front, rear = idx + 1, N - 1

    while front < rear:
        # 현재 합 계산하기
        cur_sum = liquids[idx] + liquids[front] + liquids[rear]
        
        # 최솟값 갱신하기
        if abs(cur_sum) < abs(min_sum):
            min_sum = cur_sum
            ans = [liquids[idx], liquids[front], liquids[rear]]
        
        if cur_sum == 0:
            break
        elif cur_sum < 0:
            front += 1
        else:
            rear -= 1

print(*ans)