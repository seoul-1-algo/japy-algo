import sys
sys.stdin = open('5525.txt')

N = int(input())
M = int(input()) # 문자열의 길이
chars = input()

cnt = 0
cur = 0

# for i in range(M-N):
#     if chars[i:i+2*N+1] == P:
#         cnt += 1

for i in range(M):
    if cur % 2 == 0: # 짝수면 I가 와야돼
        temp = 'I'
    else: # 홀수면 O가 와야돼
        temp = 'O'

    if chars[i] == temp: # 현재 문자가 맞게 왔으면
        cur += 1 # 인덱스 ++1

        if cur == 2 * N + 1: # P만큼 다 만들어졌다면
            cnt += 1
            cur = 2*N - 1 # 앞에 두 개 빼기

    else: # 틀림
        if chars[i] == 'I': # 현재 문자가 I이면 IOI 패턴 세기 시작 
            cur = 1
        else: # O면 리셋
            cur = 0

print(cnt)
