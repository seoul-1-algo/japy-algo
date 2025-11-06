import sys
sys.stdin = open('1351.txt')

def A(i):
    if i in memo:
        return memo[i]

    memo[i] = A(i//P) + A(i//Q)    
    return memo[i]

N, P, Q = map(int, input().split())
memo = {0: 1}
print(A(N))

# def A(i):
#     if i == 0:
#         return 1
    
#     return A(i//P) + A(i//Q)

# N, P, Q = map(int, input().split())
# print(A(N))

# import math

# N, P, Q = map(int, input().split())

# A = [0] * (N+1)

# A[0] = 1
# for i in range(1, N+1):
#     A[i] = A[i//P] + A[i//Q]

# print(A[N])