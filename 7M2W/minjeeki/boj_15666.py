def backtracking(start):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return

    for i in range(start, nums_len):
        arr.append(nums[i])
        backtracking(i)
        arr.pop()

N, M = map(int, input().split())
nums = list(set(map(int, input().split())))
nums.sort()
nums_len = len(nums)
arr = []
backtracking(0)