import sys
sys.stdin = open('15666.txt')

n, m = map(int, input().split()) # n개의 자연수 중에서 m개를 고른 수열을 찾아라
nums = list(set(map(int, input().split()))) # 같은 수 여러번 사용해도 되니까 set
nums.sort()

# print(nums)

def backtracking(arr):
    if len(arr) == m:
        print(*arr)
        return
    
    for num in nums:
        if num >= arr[-1]:
            arr.append(num)
            backtracking(arr)
            arr.pop()

for num in nums:
    backtracking([num])
