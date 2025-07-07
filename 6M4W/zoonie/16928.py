import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

movement = [i for i in range(101)]
distance = [0 for i in range(101)]
visited = [0 for i in range(101)]

for i in range(n):
    start, end = map(int,input().split())
    movement[start] = end
for i in range(m):
    start, end = map(int,input().split())
    movement[start] = end
move = deque([1])
while move:
    now = move.popleft()

    for i in range(1,7):
        next = now+i
        if next > 100:
            continue
        else:
            if visited[movement[next]] == 0:
                visited[movement[next]] = 1
                move.append(movement[next])
                distance[movement[next]] = distance[movement[now]] + 1

print(distance[100])
