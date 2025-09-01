import sys
input = sys.stdin.readline


def diffuse():
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

    # T초 동안 확산
    for t in range(T):
        diffusion = [[0] * C for _ in range(R)]     # 확산 후 미세먼지 변화량
        dusts = set()

        for r in range(R):
            for c in range(C):
                # 미세먼지 있는 칸: 확산
                if room[r][c] > 0:
                    dusts.add((r, c))
                    spread_to = 0                           # 퍼진 칸 수
                    # 상하좌우로 확산
                    for i in range(4):
                        nr, nc = r + dr[i], c + dc[i]
                        if 0 <= nr < R and 0 <= nc < C and room[nr][nc] != -1:
                            diffusion[nr][nc] += room[r][c] // 5    # 인접 칸으로 확산
                            dusts.add((nr, nc))
                            spread_to += 1
                    diffusion[r][c] -= spread_to * (room[r][c] // 5)

        # 확산 후 업데이트
        for r, c in dusts:
            room[r][c] += diffusion[r][c]

        # 공기청정기 작동
        circulate(*cleaner[0], -1)  # 위쪽 바람 순환
        circulate(*cleaner[1], 1)   # 아래쪽 바람 순환


def circulate(row, col, d):
    move_to = [d, 0]        # 다음 칸 이동 방향
    r, c = row + d, col     # 미세먼지가 이동할 칸
    while True:
        # 처음 위치로 돌아왔을 시 순환 종료
        if r == row and c == col + 1:
            room[r][c] = 0
            break

        nr, nc = r + move_to[0], c + move_to[1]     # 미세먼지가 있는 칸
        room[r][c] = room[nr][nc]                   # 이동한다.

        r, c = nr, nc

        # 순환 방향 바꾸기
        if (r == 0 or r == R - 1) and c == 0:           # <- 왼쪽으로
            move_to = [0, 1]
        elif (r == 0 or r == R - 1) and c == C - 1:     # 위 (혹은 아래)
            move_to = [-d, 0]
        elif r == row:                                  # -> 오른쪽으로
            move_to = [0, -1]


R, C, T = map(int, input().split())
room = []
cleaner = []
for i in range(R):
    row = list(map(int, input().split()))
    for j in range(C):
        if row[j] < 0:
            cleaner.append((i, j))
    room.append(row)

diffuse()
answer = 0
for row in range(R):
    answer += sum(room[row])

print(answer + 2)   # 공기청정기만큼 더한 값을 출력
