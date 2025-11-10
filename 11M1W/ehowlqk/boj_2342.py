import sys

sys.setrecursionlimit(10**6)

# input = open('boj_2342.txt', 'r').readline
arr = list(map(int, input().split()))
memo = {}   # 메모이제이션용 딕셔너리

def cost(curr, dest):
    if curr == dest:
        return 1
    if curr == 0:
        return 2
    if abs(curr - dest) == 2:
        return 4
    return 3


def solve(left, right, i):
    
    if (left, right, i) in memo:
        return memo[(left, right, i)]

    nxt = arr[i]
    if nxt == 0:
        return 0

    left_move  = solve(nxt, right, i + 1) + cost(left, nxt)     # 왼발 움직이기
    right_move = solve(left, nxt, i + 1) + cost(right, nxt)     # 오른발 움직이기
    res = min(left_move, right_move)

    memo[(left, right, i)] = res    # 메모하기
    return res


print(solve(0, 0, 0))
