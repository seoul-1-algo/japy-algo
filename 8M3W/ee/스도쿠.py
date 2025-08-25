import sys

def get_possible_numbers(board, row, col):
    """해당 위치에 올 수 있는 숫자들을 반환"""
    if board[row][col] != 0:
        return []
    
    used = set()
    
    # 같은 행의 숫자들
    for c in range(9):
        if board[row][c] != 0:
            used.add(board[row][c])
    
    # 같은 열의 숫자들
    for r in range(9):
        if board[r][col] != 0:
            used.add(board[r][col])
    
    # 같은 3x3 박스의 숫자들
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if board[r][c] != 0:
                used.add(board[r][c])
    
    # 1~9 중에서 사용되지 않은 숫자들 반환
    return [num for num in range(1, 10) if num not in used]

def is_valid(board, row, col, num):
    """해당 위치에 숫자를 놓을 수 있는지 확인"""
    # 같은 행에 있는지 확인
    for c in range(9):
        if board[row][c] == num:
            return False
    
    # 같은 열에 있는지 확인
    for r in range(9):
        if board[r][col] == num:
            return False
    
    # 같은 3x3 박스에 있는지 확인
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if board[r][c] == num:
                return False
    
    return True

def solve_sudoku(board):
    """스도쿠를 해결하는 백트래킹 함수"""
    # 빈 칸 찾기 (사전식 순서로)
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # 가능한 숫자들을 1부터 9까지 순서대로 시도 (사전식)
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        
                        if solve_sudoku(board):
                            return True
                        
                        # 백트래킹
                        board[row][col] = 0
                
                return False
    
    return True  # 모든 칸이 채워짐

# 입력 읽기
board = []
for i in range(9):
    line = input().strip()
    row = [int(digit) for digit in line]
    board.append(row)

# 스도쿠 해결
solve_sudoku(board)

# 결과 출력
for row in board:
    print(''.join(map(str, row)))