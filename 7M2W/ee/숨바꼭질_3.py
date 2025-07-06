import sys
sys.stdin = open('13549.txt')

from collections import deque

n, k = map(int, input().split()) # 수빈이 n, 동생 k

visited = [False] * 100001

q = deque()
q.append([n, 0])
visited[n] = True

while q:
    pos, sec = q.popleft()

    if pos == k:
        print(sec)
        break

    # 순간이동
    if 0 <= pos * 2 <= 100000 and not visited[pos * 2]:
        q.append([pos * 2, sec])
        visited[pos * 2] = True
    
    # 걷기
    for move in [pos - 1, pos + 1]:
        if 0 <= move <= 100000 and not visited[move]:
            q.append([move, sec + 1])
            visited[move] = True