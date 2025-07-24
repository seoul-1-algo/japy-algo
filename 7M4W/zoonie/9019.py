import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for i in range(t):
    a,b = map(int,input().split())
    queue = deque([[a,'']])
    visited = [0 for i in range(10001)]
    visited[a] = 1
    while queue:
        now = queue.popleft()
        if now[0] == b:
            print("".join(now[1]))
            break
        else:
            d = (2*now[0])%10000
            s = (now[0]-1)%10000
            l = (now[0]%1000)*10+(now[0]//1000)
            r = (now[0]%10)*1000+(now[0]//10)
            if not visited[d]:
                queue.append([d,now[1]+'D'])
                visited[d] = 1
            if not visited[s]:
                queue.append([s,now[1]+'S'])
                visited[s] = 1
            if not visited[l]:
                queue.append([l,now[1]+'L'])
                visited[l] = 1
            if not visited[r]:
                queue.append([r,now[1]+'R'])
                visited[r] = 1