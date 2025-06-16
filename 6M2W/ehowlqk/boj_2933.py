from collections import deque

r, c = map(int, input().split())
cave = [list(input()) for _ in range(r)]
n = int(input())
heights = list(map(int, input().split()))
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

# 던져서 미네랄 개기
def throw(height, turn):
    if turn % 2 == 0:
        try:
            col = cave[height].index('x')
            cave[height][col] = '.'
            return [height, col]
        except:
            return
    else:
        try:
            col = c - 1 - list(reversed(cave[height])).index('x')
            cave[height][col] = '.'
            return [height, col]
        except:
            return

# 클러스터 처리
def cluster(coor, turn):
    row, col = coor

    for i in range(4):
        if 0 <= row + dr[i] < r and 0 <= col + dc[i] < c and cave[row + dr[i]][col + dc[i]] == 'x':
            # 깨져서 분리되는 클러스터 찾기
            broken = find([row + dr[i], col + dc[i]])
            if broken:
                # 떨어뜨리기
                drop(broken)


def find(coor):
    result = [list() for _ in range(c)]     # 함수가 반환할 리스트
    result[coor[1]].append(coor[0])         # 시작위치
    q = deque()
    q.append(coor)

    visited = [[False for _ in range(c)] for _ in range(r)]
    visited[coor[0]][coor[1]] = True

    # BFS
    while q:
        row, col = q.popleft()
        # 땅과 연결되어있을 경우 return
        if row == r-1:
            return []
        for i in range(4):
            nr, nc = row + dr[i], col + dc[i]
            if 0 <= nr < r and 0 <= nc < c and not visited[nr][nc] and cave[nr][nc] == 'x':
                q.append([nr, nc])
                result[nc].append(nr)
                visited[nr][nc] = True

    # 정렬 후 return -> 나중에 가장 아래에 있는 위치 파악하기 위해
    for _list in result:
        _list.sort()
    return result


def drop(coors):
    # coors: 분리되는 클러스터 덩어리들 좌표(coors 내 인덱스 k = 열, k번재 배열 내 숫자 = 행)
    step = 0
    stop = False
    while not stop:
        for i in range(c):
            if coors[i]:
                descend = coors[i][-1] + step + 1
                # 바닥이나 다른 미네랄에 도달한 경우: stop
                if descend == r or cave[descend][i] == 'x':
                    stop = True
                    break

        if stop:
            break
        # 한칸 더 아래로
        step += 1

    if step == 0:
        return

    # 클러스터 위치 옮기기

    for i in range(c):
        for row in coors[i]:
            cave[row][i] = '.'

    for i in range(c):
        for row in coors[i]:
            cave[row + step][i] = 'x'


for i in range(n):
    coor = throw(r - heights[i], i)     # 미네랄 깨진 위치
    if coor:
        # 깨진 위치 기준 클러스터 처리하기
        cluster(coor, i)

# 결과 출력
for row in cave:
    print("".join(row))
