import sys
sys.stdin = open('1561.txt')

N, M = map(int, input().split()) # 아이들의 수 N, 놀이기구의 수 M
durations = list(map(int, input().split())) # 놀이기구의 운행 시간

# 시간 t분이 지났을 때 몇 명이 탔는지
# total = M명 + sum(t // durations[i] for i in range(M))

# total이 N이 될 때를 찾으면 됨

left = 0
right = 6e10 # 충분히 큰 값

while left <= right:
    mid = (left + right) // 2

    # mid분까지 놀이기구를 탄 아이들 수
    total = M + sum(mid // duration for duration in durations)

    if total >= N: # N번째 아이가 탈 수 있으면
        t = mid 
        right = mid - 1
    else: # N번째 아이까지 못 태움
        left = mid + 1

# t : N번째 아이가 타는 최소 시간
# 그 직전 시점(t - 1)까지 몇 명이 탔는 지
temp_cnt = M + sum((t- 1) // duration for duration in durations)

# t 시점에 놀이기구 몇 개가 비는 지 확인
for i, d in enumerate(durations):
    if t % d == 0: # 해당 놀이기구는 t 시점에 비어있음
        temp_cnt += 1
        if temp_cnt == N: # N번째 아이 !!!!!!
            print(i + 1) # 놀이기구 번호 출력
            break
