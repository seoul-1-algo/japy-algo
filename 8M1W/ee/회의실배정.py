import sys
sys.stdin = open('1931.txt')

N = int(input())

conferences = []

for i in range(N):
    s, e = map(int, input().split()) # 회의의 시작시간, 끝나는 시간
    conferences.append((s, e))

conferences.sort(key = lambda x: (x[1], x[0]))

# print(conferences)

cnt = 0 # 회의 개수

prev_end = 0
for cur_start, cur_end in conferences:
    # 아직 회의가 안 끝났으면
    if prev_end > cur_start:
        continue
    
    # 이전 회의가 끝났으면
    prev_end = cur_end
    cnt += 1

print(cnt)