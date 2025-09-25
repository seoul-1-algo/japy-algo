from collections import deque

n = int(input())
sea = [list(map(int,input().split())) for _ in range(n)]

now_i, now_j = 0, 0
for i in range(n):
    for j in range(n):
        if sea[i][j] == 9:
            sea[i][j] = 0
            now_i, now_j = i, j

shark_size = 2
hungry = 2
t = 0

# 먹을 후보 탐색 우선순위 위, 왼쪽, 오른쪽, 아래
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def find_target(si, sj):
    """현재 위치(si,sj)에서 먹을 수 있는 물고기 중
       최소 거리 후보들을 모아 (행,열) 오름차순으로 하나 반환.
       없으면 None 반환. 결과: (ti, tj, dist)"""
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append((si, sj, 0))
    visited[si][sj] = True

    min_dist = None
    candidates = []

    while q:
        x, y, d = q.popleft()

        # 이미 최소거리 후보가 있으면 그보다 깊게는 안 내려감
        if min_dist is not None and d > min_dist:
            break

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 이동 가능(같은 크기는 통과만 가능)
                if sea[nx][ny] <= shark_size:
                    visited[nx][ny] = True
                    nd = d + 1
                    # 먹기 가능?
                    if 0 < sea[nx][ny] < shark_size:
                        if min_dist is None:
                            min_dist = nd
                        if nd == min_dist:
                            candidates.append((nx, ny))
                    else:
                        # 빈칸/같은크기 → 계속 탐색
                        q.append((nx, ny, nd))

    if not candidates:
        return None
    candidates.sort()  # (행,열) 오름차순 → 위/왼 우선
    ti, tj = candidates[0]
    return (ti, tj, min_dist)

while True:
    res = find_target(now_i, now_j)
    if res is None:
        break

    ti, tj, dist = res
    # 이동 시간 누적
    t += dist

    # 먹기
    sea[ti][tj] = 0
    hungry -= 1
    now_i, now_j = ti, tj

    if hungry == 0:
        shark_size += 1
        hungry = shark_size

print(t)
