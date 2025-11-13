import sys
sys.stdin = open('1766.txt')

from heapq import heappush, heappop

input = sys.stdin.readline
N, M = map(int, input().split()) # N: 문제의 수, M: 문제에 대한 정보의 개수

solving_order = [[] for _ in range(N+1)]
indeg = [0] * (N+1) # 진입차수

for _ in range(M):
    A, B = map(int, input().split()) # A번 문제는 B번 문제보다 먼저 푸는 것이 좋다
    solving_order[A].append(B)
    indeg[B] += 1 # B를 풀기 전에 풀어야 하는 문제의 개수 

hq = []
for num in range(1, N+1):
    if indeg[num] == 0: # 먼저 풀어야 하는 문제가 없으면
        heappush(hq, num) # 바로 힙에 넣음

ans = []

while hq: # 힙이 빌 때 까지
    num = heappop(hq) # 가장 쉬운(번호가 작은) 문제부터 pop
    ans.append(num)

    for nxt in solving_order[num]:
        indeg[nxt] -= 1
        if indeg[nxt] == 0: # nxt번 문제 풀기 전에 풀어야 하는 문제 다 풀었으면
            heappush(hq, nxt) # nxt도 힙에 추가

print(*ans)