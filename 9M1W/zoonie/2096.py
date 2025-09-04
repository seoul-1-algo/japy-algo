import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
max_dp = nums
min_dp = nums

for i in range(1,n):
    now_line = list(map(int,input().split()))
    a,b,c = 0,0,0
    a = max(max_dp[0],max_dp[1]) + now_line[0]
    b = max(max_dp[0],max_dp[1],max_dp[2]) + now_line[1]
    c = max(max_dp[1],max_dp[2]) + now_line[2]

    max_dp = [a,b,c]


    d,e,f = 0,0,0
    d = min(min_dp[0],min_dp[1]) + now_line[0]
    e = min(min_dp[0],min_dp[1],min_dp[2]) + now_line[1]
    f = min(min_dp[1],min_dp[2]) + now_line[2]

    min_dp = [d,e,f]

print(max(max_dp), min(min_dp))