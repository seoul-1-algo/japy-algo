import sys
sys.stdin = open("2933.txt")

from collections import deque

R, C = map(int, input().split())
cave = [list(input()) for _ in range(R)]

N = int(input()) # 막대를 던진 횟수
heights = list(map(int, input().split()))

# 1. 미네랄 부시기
# 2. 상하좌우 체크해서 공중에 떠 있는지 확인
# 3. 공중에 떠 있으면 클러스터 낙하

def throw(row, is_left):
    if is_left: # 왼쪽에서 던지면
        for col in range(C):
            if cave[row][col] == 'x':
                cave[row][col] = '.' # 부시기
                return row, col
    else: # 오른쪽에서 던지면
        for col in range(C-1, -1, -1):
            if cave[row][col] == 'x':
                cave[row][col] = '.' # 부시기
                return row, col
    return -1, -1

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def check_cluster(row, col):
    visited = [[False] * C for _ in range(R)]
    q = deque()
    q.append((row, col))
    visited[row][col] = True

    cluster = [(row, col)]

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < R and 0 <= nc < C:
                if cave[nr][nc] == 'x' and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    cluster.append((nr, nc))
    
    return cluster

def check_float(cluster):
    cluster_set = set(cluster)
    for row, col in cluster:
        # 바닥에 닿았거나, 클러스터 밖 'x'와 닿았으면 떠 있는 게 아님
        if row == R - 1 or (cave[row + 1][col] == 'x' and (row + 1, col) not in cluster_set):
            return False
    return True


def fall(cluster):
    # 지워
    for r, c in cluster:
        cave[r][c] = '.'

    # cluster를 아래로 한 칸씩 내릴 수 있을 때까지 반복
    can_fall = True
    while True:
        for r, c in cluster:
            nr = r + 1
            # 바닥에 닿거나, 다른 미네랄 위면 못 떨어짐
            if nr >= R or (cave[nr][c] == 'x' and (nr, c) not in cluster):
                can_fall = False
                break
        if not can_fall:
            break
        # 한 칸 내리기
        cluster = [(r+1, c) for r, c in cluster]

    # 다시 cave에 채워넣기
    for r, c in cluster:
        cave[r][c] = 'x'

for i in range(N):
    height = heights[i]
    is_left = i % 2

    r, c = throw(R- height, is_left)
    print(r, c)
    if r == -1:
        continue

    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < R and 0 <= nc < C and cave[nr][nc] == 'x':
            cluster = check_cluster(nr, nc) 
            print(cluster)
            if check_float(cluster): # 클러스터가 떠 있으면
                fall(cluster) # 추락시켜ㅕㅕ

for row in cave:
    print(''.join(row))