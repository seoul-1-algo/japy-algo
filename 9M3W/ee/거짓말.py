import sys
sys.stdin = open('1043.txt')

from collections import deque

N, M = map(int, input().split()) # 사람의 수 N, 파티의 수 M

truth = list(map(int, input().split())) # 이야기의 진실을 아는 사람

people = [[] for _ in range(N + 1)] # i 사람이 참석한 파티의 인덱스를 저장
parties = [[] for _ in range(M)] # i 파티에 참석한 사람들의 인덱스를 저장

for idx in range(M):
    participants = list(map(int, input().split()))

    cnt_participants = participants[0]
    participants = participants[1:]

    parties[idx] = participants

    for p in participants:
        people[p].append(idx)

people_visited = [False] * (N+1)
party_visited = [False] * M

q = deque([])

truth_cnt = truth[0]
if truth_cnt > 0:
    for t in range(1, truth_cnt + 1):
        people_visited[truth[t]] = True # 이 사람은 진실을 알고 있다
        q.append(truth[t]) # 큐에 추가

while q:
    cur_person = q.popleft()

    for idx in people[cur_person]:
        if party_visited[idx]: # 이미 진실이 퍼진 파티면
            continue

        party_visited[idx] = True # 이 파티는 진실이 다 퍼졋다

        for person in parties[idx]: # 파티에 참석한 사람들
            if not people_visited[person]: # 아직 모르고 있으면
                people_visited[person] = True 
                q.append(person)

ans = 0
for i in range(M):
    if not party_visited[i]:
        ans += 1

print(ans)