import sys
sys.stdin = open('1987.txt')

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def go(r, c, track):
    global max_cnt

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        # 보드 범위를 벗어나지 않으면서, 지나온 칸에 동일한 알파벳이 없다면
        if 0 <= nr < R and 0 <= nc < C and board[nr][nc] not in track:
            track.add(board[nr][nc])
            max_cnt = max(max_cnt, len(track))
            go(nr, nc, track)
            track.remove(board[nr][nc])

track = set(board[0][0])
max_cnt = 1
go(0, 0, track)
print(max_cnt)