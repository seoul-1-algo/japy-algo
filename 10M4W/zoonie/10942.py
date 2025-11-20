import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
m = int(input())

palindrome = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    palindrome[i][i] = 1

for i in range(n-1):
    if nums[i]==nums[i+1]:
        palindrome[i][i+1] = 1

for length in range(2, n):
    for start in range(n - length):
        end = start + length
        if nums[start] == nums[end] and palindrome[start+1][end-1] == 1:
            palindrome[start][end] = 1

for _ in range(m):
    s,e = map(int,input().split())
    print(palindrome[s-1][e-1])