import sys
sys.stdin = open('1074.txt')

def z(n, r, c):
    if n == 0:
        return 0
    
    half = 2 ** (n - 1)
    size = half * half

    if r < half and c < half:
        return z(n - 1, r, c)
    elif r < half and c >= half:
        return size + z(n - 1, r, c - half)
    elif r >= half and c < half:
        return 2 * size + z(n - 1, r - half, c)
    else:
        return 3 * size + z(n - 1, r - half, c - half)
    
N, R, C = map(int, input().split())
print(z(N, R, C))
