n = int(input())
nums = list(map(int, input().split()))
m = int(input())
palindrome = [[int(i==j) for i in range(n+1)] for j in range(n+1)]


# 2 짜리 팰린드롬
for i in range(1, n):
    if nums[i] == nums[i-1]:
        palindrome[i][i+1] = 1

# 3 이상 팰린드롬
for l in range(3, n+1):
    for start in range(1, n - l + 2):
        end = start + l - 1
        if nums[start - 1] == nums[end - 1] and palindrome[start + 1][end - 1]:
            palindrome[start][end] = 1

for _ in range(m):
    s, e = map(int, input().split())
    print(palindrome[s][e])
