import sys
input = sys.stdin.readline

# N: 배열의 크기는 2**N x 2**N
# r: 목표 좌표의 행, c: 목표 좌표의 열
N, r, c = map(int, input().split())

ans = 0  # 방문 순서를 누적할 변수

# 배열을 분할하며 (r, c)가 어디 위치인지 찾아가는 과정
while N != 0:
    N -= 1  # 매 반복마다 배열을 4등분 (2**N → 2**(N-1))

    # 현재 크기의 절반 → 각 사분면의 한 변 길이
    size = 2 ** N

    # 1) 왼쪽 위 (Z 순서 기준 0번 사분면)
    if r < size and c < size:
        # 현재 위치는 왼쪽 위 영역이므로 누적할 방문 수 없음 (가장 앞)
        # ans += 0 은 생략해도 무방
        ans += size * size * 0

    # 2) 오른쪽 위 (Z 순서 기준 1번 사분면)
    elif r < size and c >= size:
        # 앞쪽에 있는 0번 사분면 만큼을 지나고 현재 위치 도달
        ans += size * size * 1
        # 열 기준으로 오른쪽 절반에 있으므로, 왼쪽 기준으로 좌표 보정
        # 즉, c 좌표를 오른쪽으로 size 만큼 이동한 걸 다시 0부터 시작하는 값으로 보정
        c -= size

    # 3) 왼쪽 아래 (Z 순서 기준 2번 사분면)
    elif r >= size and c < size:
        # 앞쪽의 0,1 사분면을 모두 지난 후
        ans += size * size * 2
        # 행 기준으로 아래쪽 절반에 있으므로, 위 기준으로 보정
        r -= size

    # 4) 오른쪽 아래 (Z 순서 기준 3번 사분면)
    else:
        # 앞의 3개 사분면(0~2번)을 모두 지나야 도달
        ans += size * size * 3
        # 행, 열 모두 절반만큼 내려갔으니 둘 다 보정
        r -= size
        c -= size

# 반복이 끝나면, ans에 (r, c)의 방문 순서가 저장됨
print(ans)
