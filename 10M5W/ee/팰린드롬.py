import sys
sys.stdin = open('10942.txt')

# 입력 최적화
import sys
input = sys.stdin.readline

N = int(input()) # 수열의 크기
nums = [0] + list(map(int, input().split())) # 홍준이가 칠판에 적은 수 N개

dp = [[0] * (N+1) for _ in range(N+1)]

# 자기 자신
for i in range(1, N+1):
    dp[i][i] = 1

# 두 글자가 같으면
for i in range(1, N):
    dp[i][i+1] = 1 if nums[i] == nums[i+1] else 0

# 나머지
for length in range(3, N+1):
    for s in range(1, N - length + 2):
        e = s + length - 1

        if nums[s] == nums[e] and dp[s+1][e-1]:
            dp[s][e] = 1

M = int(input()) # 질문의 개수

# 출력 최적화
ans = []
for _ in range(M):
    S, E = map(int, input().split()) 
    ans.append(str(dp[S][E]))

sys.stdout.write('\n'.join(ans))
