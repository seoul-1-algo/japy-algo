import sys
sys.stdin = open('9019.txt')

from collections import deque

T = int(input())

def reform(nums):
    return '0' * (4 - len(str(nums))) + str(nums)

def D(nums):
    nums *= 2
    if nums > 9999:
        nums %= 10000
    return nums

def S(nums):
    if nums == 0:
        nums = 9999
    else:
        nums -= 1
    return nums

def L(nums):
    chars = reform(nums)
    return int(chars[1] + chars[2] + chars[3] + chars[0])

def R(nums):
    chars = reform(nums)
    return int(chars[3] + chars[0] + chars[1] + chars[2])


def bfs(A, B):
    q = deque([('', A)])
    visited = [False] * 10000

    while q:
        cmd, nums = q.popleft()

        if nums == B:
            print(cmd)
            return
        
        if not visited[nums]:
            
            visited[nums] = True

            d, s, l, r = D(nums), S(nums), L(nums), R(nums)

            if not visited[d]:
                q.append((cmd + 'D', d))

            if not visited[s]:
                q.append((cmd + 'S', s))

            if not visited[l]:
                q.append((cmd + 'L', l))

            if not visited[r]:
                q.append((cmd + 'R', r))

for _ in range(T):
    A, B = map(int, input().split())
    bfs(A, B)
