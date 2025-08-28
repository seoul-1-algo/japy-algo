import sys

sys.stdin = open('boj_17143.txt')
input = sys.stdin.readline

R, C, M = map(int, input().split())
sharks = dict()     # key: 상어 크기 / value: [열, 행, 속력, 방향]
graph = [[[] for _ in range(C)] for _ in range(R)]      # 격자판 -> 각 격자의 원소: 상어 크기 배열

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks[z] = [r, c, s, d]
    graph[r-1][c-1].append(z)

def move_shark(r, c, s, d):
    coor = [r, c]
    
    if d == 1:  # 상
        limit = R - 1
        curr = r
        move = -s

    elif d == 2:    # 하
        limit = R - 1
        curr = r
        move = s

    elif d == 3:    # 우
        limit = C - 1
        curr = c
        move = s

    else:   # 좌
        limit = C - 1
        curr = c
        move = -s

    next, nd = nextLoc(curr, move, limit, d)
    coor[d // 3] = next # 1, 2 -> 열 이동 / 3, 4 -> 행 이동
    return [*coor, nd]  # 새로운 위치와 방향 return


def nextLoc(curr, move, limit, d):
    nd = d
    remainder = (curr + move - 1) % (2 * limit) # zero-base 처리
    # 방향 유지하는 경우
    if remainder < limit:
        next = remainder + 1
    # 반사돼서 방향 바뀌는 경우
    else:
        next = limit - (remainder - limit) + 1
        nd += 1 if d % 2 else -1
    
    return (next, nd)

answer = 0
for col in range(1, C + 1):
    # 가장 가까운 행의 상어 잡기
    for row in range(R):
        if graph[row][col - 1]:
            key = graph[row][col - 1][0]
            del sharks[key]
            answer += key
            graph[row][col - 1] = []
            break

    # 상어 이동
    del_list = []   # 둘 이상의 상어가 있는 위치를 저장
    for z in sharks:
        r, c, s, d = sharks[z]
        nr, nc, nd = move_shark(r, c, s, d)
        node = graph[nr - 1][nc - 1]
        
        # 현재 칸에 이미 상어가 있다면 del_list에 위치 추가
        if node:
            del_list.append((nr, nc))
        graph[r - 1][c - 1].remove(z)
        graph[nr - 1][nc - 1].append(z)
        sharks[z] = [nr, nc, s, nd]

    # 같은 위치에 있는 상어 처리하기 
    for r, c in del_list:
        max_size = max(graph[r - 1][c - 1])     # 가장 큰 상어의 크기
        for shark in graph[r - 1][c - 1]:
            if shark < max_size: del sharks[shark]  # 작은 애들 다 잡아먹는다
        
        graph[r - 1][c - 1] = [max_size]    # graph 갱신
    
print(answer)
