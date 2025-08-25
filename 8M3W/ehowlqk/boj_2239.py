def backtracking(row, col):
    # 마지막 depth에 도달했다면 정답 출력
    if row == 9:
        for line in sudoku:
            print(line, sep='')
        return True

    next = [row, col + 1] if col < 8 else [row + 1, 0]
    if sudoku[row][col] == 0:
        # 열, 행, 블록 체크 -> 가능한 숫자 목록 뽑기
        candidates = check(row, col)
        for candidate in candidates:
            sudoku[row][col] = candidate
            check_row[row].append(candidate)
            check_col[col].append(candidate)
            check_block[row//3][col//3].append(candidate)
            if backtracking(next[0], next[1]):
                return True
            sudoku[row][col] = 0
            check_row[row].pop()
            check_col[col].pop()
            check_block[row//3][col//3].pop()
    else:
        return backtracking(next[0], next[1])


def check(row, col):
    filter = check_row[row] + check_col[col] + check_block[row//3][col//3]
    return [x for x in range(1, 10) if x not in set(filter)]


sudoku, check_row, check_col, check_block = [], [[] for _ in range(9)], [[] for _ in range(9)], [[[] for _ in range(3)] for _ in range(3)]

for i in range(9):
    line = list(map(int, input()))
    sudoku.append(line)
    for j in range(9):
        # 각 행, 열, 블록 별 사용된 숫자 기록
        if line[j] > 0:
            check_row[i].append(line[j])
            check_col[j].append(line[j])
            check_block[i//3][j//3].append(line[j])

backtracking(0, 0)
