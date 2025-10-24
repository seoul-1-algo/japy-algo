import sys
input = sys.stdin.readline
N, S = map(int, input().split())
arr = list(map(int, input().split()))
total = 0   # start, end 구간의 원소 합
start = 0
end = 0 
min_len = 1e9
while True:
    if total >= S:  # 현재 구간합이 S이상이므로
        min_len = min(min_len, end - start) # 최솟값 찾기
        total -= arr[start] 
        start += 1  # start 줄이기
    
    elif total < S: # 현재 구간합이 S보다 작으므로
        if end == len(arr):
            break   # 더 이상 불가능하므로 끄읏
        total += arr[end]
        end += 1

if min_len == 1e9:  # 아예 불가능
    print(0)
else:
    print(min_len)
