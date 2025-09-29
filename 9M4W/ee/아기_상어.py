import sys
sys.stdin = open('16236.txt')

from collections import deque

N = int(input())  # 공간의 크기
arr = [list(map(int, input().split())) for _ in range(N)]  # 공간의 상태

fish_pos = [] 
time = 0 

for x in range(N):
    for y in range(N):
        if arr[x][y] == 9:
            shark_pos = (x, y)
            arr[x][y] = 0 

shark_size = 2
eat_cnt = 0

di = [-1, 0, 0, 1]
dj = [0, -1, 1, 0]


def calculate_distance(si, sj, size):
    q = deque([(si, sj, 0)]) 
    visited = [[False] * N for _ in range(N)]
    visited[si][sj] = True

    fish = []
    min_dist = -1

    while q:
        i, j, dist = q.popleft()

        if dist > min_dist >= 0:
            break

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:

                if arr[ni][nj] <= size:
                    visited[ni][nj] = True
                    next_dist = dist + 1

                    # 먹을 수 있는 물고기 추가
                    if 0 < arr[ni][nj] < size:
                        fish.append((next_dist, ni, nj))
                        if min_dist == -1:
                            min_dist = next_dist

                    q.append((ni, nj, next_dist))

    if not fish:
        return None

    fish.sort() 
    return fish[0] 

def decide_direction():
    si, sj = shark_pos
    next_fish = calculate_distance(si, sj, shark_size)
    return next_fish 

while True:
    next_fish = decide_direction()

    if next_fish is None:
        break

    dist, fi, fj = next_fish

    time += dist
    shark_pos = (fi, fj)
    arr[fi][fj] = 0
    eat_cnt += 1

    if eat_cnt == shark_size:
        shark_size += 1
        eat_cnt = 0

print(time)
