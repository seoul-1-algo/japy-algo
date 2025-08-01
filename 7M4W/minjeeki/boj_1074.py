N, r, c = map(int, input().split())

def find_num(N, r, c):
    if N == 0:
        return 0
    
    # 4등분 할 경우 한 변의 길이
    size = 2 ** (N - 1)
    # 현재 좌표의 위치 파악
    row, col = r // size, c // size
    
    num = 0
    # 왼쪽 위
    if row == 0 and col == 0:
        num = find_num(N - 1, r, c)
    # 오른쪽 위
    elif row == 0 and col == 1:
        num = size ** 2 + find_num(N - 1, r, c - size)
    # 왼쪽 아래
    elif row == 1 and col == 0:
        num = 2 * size ** 2 + find_num(N - 1, r - size, c)
    # 오른쪽 아래
    else:
        num = 3 * size ** 2 + find_num(N - 1, r - size, c - size)
    
    return num

print(find_num(N, r, c))