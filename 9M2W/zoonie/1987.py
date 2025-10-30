from collections import deque
import copy

r,c = map(int,input().split())

array = [list(input()) for i in range(r)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

check = [0 for i in range(26)]
check[ord(array[0][0])-65] = 1
queue = deque([[0,0,check]])
ans = 1
while queue:
    nowx, nowy, nowcheck = queue.pop()
    newcheck = copy.deepcopy(nowcheck)
    print(nowx,nowy,newcheck)
    for i in range(4):
        if 0<=nowx+dx[i]<r and 0<=nowy+dy[i]<c:
            if newcheck[ord(array[nowx+dx[i]][nowy+dy[i]])-65] == 0:
                newcheck[ord(array[nowx+dx[i]][nowy+dy[i]])-65] = 1
                ans = max(ans,sum(newcheck))
                queue.append([nowx+dx[i],nowy+dy[i],newcheck])

print(ans)




