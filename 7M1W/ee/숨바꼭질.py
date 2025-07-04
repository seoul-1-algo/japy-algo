import sys
sys.stdin = open("1697.txt")

from collections import deque
N, K = map(int, input().split()) # N: 수빈이, K: 휴닝이

# 점 X로 올 수 있는 방법 
# 1. X+1에서 -1해서 오기
# 2. X-1에서 +1해서 오기
# 3. X/2에서 *2해서 오기

# dp로 풀고 싶었지만? 되지않는다 .

visited = [False] * 100001

q = deque()
q.append([N, 0]) # [수빈 위치, 시간]
visited[N] = True

while q:
    pos, sec = q.popleft()

    if pos == K: # 수빈이랑 동생이랑 만나면
        print(sec) # 시간 출력
        break

    for move in [pos + 1, pos - 1, pos * 2]:
        if 0 <= move <= 100000 and not visited[move]:
            q.append([move, sec + 1])
            visited[move] = True