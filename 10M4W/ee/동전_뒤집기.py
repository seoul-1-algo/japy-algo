import sys
sys.stdin = open('1285.txt')

N = int(input())
coins = list(list(input()) for _ in range(N)) # 동전 초기 상태

# T, H를 0, 1로 변환해서 저장
for i in range(N):
    for j in range(N):
        coins[i][j] = 1 if coins[i][j] == 'T' else 0

ans = 1e10

for bitmask in range(1 << N):
    # 복사
    tmp = [row[:] for row in coins]

    # 행 뒤집기
    for row in range(N):
        if bitmask & (1 << row):
            for col in range(N):
                tmp[row][col] ^= 1

    # 열 뒤집기
    total = 0
    
    for col in range(N):
        cnt = sum(tmp[row][col] for row in range(N))
        total += min(cnt, N - cnt)

    ans = min(ans, total)

print(ans)