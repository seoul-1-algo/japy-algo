import sys
sys.stdin = open('1566.txt')

from copy import deepcopy

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

min_val = 1000

def check_p_arr(cur_arr):
    # 행 체크
    for row in cur_arr:
        # print(sum(row))
        if sum(row) <= 0:
            return False
        
    # 열 체크
    for j in range(M):
        temp = 0
        for i in range(N):
            temp += cur_arr[i][j]
        if temp <= 0:
            return False
    
    return True

def reverse_col(col, cur_arr, cnt):
    global min_val

    # 종료 조건
    if col == M:
        if check_p_arr(cur_arr):
            min_val = min(min_val, cnt)
        return

    reverse_col(col+1, cur_arr, cnt)

    new_arr = deepcopy(cur_arr)
    for r in range(N):
        new_arr[r][col] *= -1

    reverse_col(col+1, new_arr, cnt+1)
        

def reverse_row(row, cur_arr, cnt):
    # 종료 조건
    if row == N:
        reverse_col(0, cur_arr, cnt)
        return
    
    # 현재 행을 뒤집지 않고 다음행으로!!!
    reverse_row(row+1, cur_arr, cnt)

    # 현재 행을 뒤집고 다음행으로!!!
    new_arr = deepcopy(cur_arr)
    new_arr[row] = [-x for x in new_arr[row]]

    reverse_row(row+1, new_arr, cnt+1)


reverse_row(0, arr, 0)
print(min_val if min_val != 1000 else -1)
