from collections import deque
import sys
input = sys.stdin.readline

# 방향 벡터 (상, 하, 좌, 우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# ========================================
# 1. 막대 던지기
# - 주어진 높이에서 'x' 하나를 제거 (왼→오 또는 오→왼)
# ========================================
def throw_stick(cave, R, C, height, from_left):
    row = R - height
    cols = range(C) if from_left else reversed(range(C))
    for col in cols:
        if cave[row][col] == 'x':
            cave[row][col] = '.'  # 미네랄 제거
            return (row, col)     # 깨진 위치 반환
    return None

# ========================================
# 2. 바닥 클러스터 확인
# - cave의 가장 아래줄부터 BFS로 이어진 'x'를 모두 visited 처리
# ========================================
def mark_ground_cluster(cave, R, C):
    visited = [[False] * C for _ in range(R)]
    queue = deque()

    for col in range(C):
        if cave[R-1][col] == 'x' and not visited[R-1][col]:
            visited[R-1][col] = True
            queue.append((R-1, col))

    while queue:
        r, c = queue.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and cave[nr][nc] == 'x':
                visited[nr][nc] = True
                queue.append((nr, nc))
    return visited

# ========================================
# 3. 공중 클러스터 탐색
# - 부서진 위치의 인접 4방향에서 떨어진 클러스터 찾기
# - BFS로 클러스터 수집 후 일시적으로 '.' 처리
# ========================================
def find_floating_cluster(cave, visited, R, C, start):
    r, c = start
    if not (0 <= r < R and 0 <= c < C) or cave[r][c] != 'x' or visited[r][c]:
        return None

    cluster = []
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True
    cluster.append((r, c))
    cave[r][c] = '.'  # 제거

    while queue:
        cr, cc = queue.popleft()
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and cave[nr][nc] == 'x':
                visited[nr][nc] = True
                queue.append((nr, nc))
                cluster.append((nr, nc))
                cave[nr][nc] = '.'  # 제거
    return cluster

# ========================================
# 4-1. 낙하 거리 계산
# - 클러스터를 아래로 몇 칸까지 떨어뜨릴 수 있는지 계산
# ========================================
def compute_fall_distance(cave, cluster, R, C, visited):
    cluster_set = set(cluster)
    min_dist = R
    for r, c in cluster:
        nr = r + 1
        dist = 0
        while nr < R:
            if cave[nr][c] == 'x' and visited[nr][c]:  # 바닥 클러스터와 충돌
                break
            if (nr, c) in cluster_set:  # 같은 클러스터면 무시
                nr += 1
                continue
            if cave[nr][c] == 'x':  # 다른 클러스터 충돌
                break
            dist += 1
            nr += 1
        min_dist = min(min_dist, dist)
    return min_dist

# ========================================
# 4-2. 낙하 적용
# - 클러스터를 계산된 거리만큼 아래로 이동하여 cave에 반영
# ========================================
def apply_fall(cave, cluster, fall_distance):
    for r, c in sorted(cluster, reverse=True):  # 밑에서부터 채워야 겹치지 않음
        cave[r + fall_distance][c] = 'x'

# ========================================
# 클러스터 낙하 전체 처리
# - 부서진 위치에서 4방향 탐색하여 공중 클러스터 찾고 낙하
# ========================================
def handle_cluster_fall(cave, R, C, broken_pos):
    visited = mark_ground_cluster(cave, R, C)

    for d in range(4):
        nr, nc = broken_pos[0] + dr[d], broken_pos[1] + dc[d]
        if 0 <= nr < R and 0 <= nc < C:
            if cave[nr][nc] == 'x' and not visited[nr][nc]:
                floating_cluster = find_floating_cluster(cave, visited, R, C, (nr, nc))
                if floating_cluster:
                    fall_dist = compute_fall_distance(cave, floating_cluster, R, C, visited)
                    apply_fall(cave, floating_cluster, fall_dist)
                break  # 하나만 떨어짐

# ========================================
# 5. main: 막대 투척 → 클러스터 확인 → 낙하 → 출력
# ========================================
R, C = map(int, input().split())
cave = [list(input().strip()) for _ in range(R)]
N = int(input())
throws = list(map(int, input().split()))

for i in range(N):
    height = throws[i]
    from_left = (i % 2 == 0)  # 짝수: 왼쪽 → 오른쪽
    broken = throw_stick(cave, R, C, height, from_left)
    if broken:
        handle_cluster_fall(cave, R, C, broken)

# 최종 출력
for row in cave:
    print(''.join(row))
