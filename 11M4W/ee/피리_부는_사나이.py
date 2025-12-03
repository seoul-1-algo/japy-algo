import sys
sys.stdin = open('16724.txt')

N, M = map(int, input().split()) # 지도의 행 N, 열 M
arr = [list(input()) for _ in range(N)] # 지도의 정보

visited = [[0] * M for _ in range(N)]

# 성우가 정해놓은 방향대로 움직일 위치를 반환하는 함수
def move(r, c):
    if arr[r][c] == 'U':
        return r-1, c
    elif arr[r][c] == 'D':
        return r+1, c
    elif arr[r][c] == 'L':
        return r, c-1
    else: # 'R'일 때
        return r, c+1

def dfs(r, c):
    global ans

    visited[r][c] = 1 # 방문 중
    nr, nc = move(r, c) # 다음 이동 위치

    if visited[nr][nc] == 1: # 사이클 발생
        ans += 1
        
    elif visited[nr][nc] == 0: # 아직 방문하지 않았으면
        dfs(nr, nc)

    visited[r][c] = 2 # 방문 완료 처리

ans = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            dfs(i, j)

print(ans)