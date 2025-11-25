import sys
sys.stdin = open('1091.txt')

# S 배열에 의해 카드를 섞는 함수
def move(arr):
    new_arr = [0] * N

    for i in range(N):
        new_arr[S[i]] = arr[i]

    return new_arr

# 현재 카드 배열이 최종적으로 와야하는 배열 상태인지 확인하는 함수
def check(arr):
    # arr[pos] : 현재 pos에 놓여있는 카드가 가야하는 플레이어 번호
    # pos % 3 : 이 위치에서 실제로 카드를 받는 플레이어 번호
    for pos in range(N):
        if arr[pos] != pos % 3:
            return False
    return True

# 입력 받기
N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))

players = P[:] # 현재 위치에 있는 카드가 최종적으로 가야하는 플레이어의 번호를 저장하는 배열
start = players[:] # 처음 상태

ans = 0 # 섞은 횟수 
while True:
    # 종료 조건
    if check(players):
        print(ans)
        break

    if ans > 0 and players == start: # 한 번 이상 섞었고, 다시 처음 상태로 돌아온 경우
        print(-1)
        break

    # 다르면 섞는다
    players = move(players)
    ans += 1