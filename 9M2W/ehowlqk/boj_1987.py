import sys
input = sys.stdin.readline

R, C = map(int, input().split())

# 백트래킹 풀이(PyPy 통과)
# alphabets = [list(input()) for _ in range(R)]
# dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
# def backtracking(r, c, depth, used):
#     answer = depth
#     for i in range(4):
#         nr, nc = r + dr[i], c + dc[i]
#         if 0 <= nr < R and 0 <= nc < C and alphabets[nr][nc] not in used:
#             used.add(alphabets[nr][nc])
#             answer = max(answer, backtracking(nr, nc, depth + 1, used))
#             used.remove(alphabets[nr][nc])
#
#     return answer


# print(backtracking(0, 0, 1, set(alphabets[0][0])))

# 보드를 비트로 전처리 (대문자 기준: 'A'->0)
board = [[1 << (ord(ch) - 65) for ch in input().strip()] for _ in range(R)]
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

best = 1
start_mask = board[0][0]

# 스택: (r, c, mask, depth)
stack = [(0, 0, start_mask, 1)]
seen_depth = {(0, 0, start_mask): 1}

while stack:
    r, c, mask, depth = stack.pop()
    if depth > best:
        best = depth
        if best == 26:     # 알파벳 최대치 도달 시 즉시 종료
            break

    m = mask
    for dr, dc in dirs:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < R and 0 <= nc < C:
            bit = board[nr][nc]
            if (m & bit) == 0:
                nm = m | bit
                nd = depth + 1
                # 가지치기: 같은 상태를 더 짧게 온 적 있으면 스킵
                key = (nr, nc, nm)
                if seen_depth.get(key, 0) >= nd:
                    continue
                seen_depth[key] = nd
                stack.append((nr, nc, nm, nd))

print(best)
