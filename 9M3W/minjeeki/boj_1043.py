# N : 사람 수 / M : 파티 수
N, M = map(int, input().split())
lst = list(map(int, input().split()))
cnt, known_lst = lst[0], lst[1:]

# 리더 배열, 경로 압축을 위한 랭크 배열
parent = list(range(N + 1))
rank = [0] * (N + 1)

# 리더 찾기
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

# 리더 합치기
def union(a, b):
    ra, rb = find(a), find(b)
    # 리더가 같다면 합치지 않음
    if ra == rb: return
    # 랭크가 더 높은 리더를 리더로 설정
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    # 랭크가 같다면 리더를 합치고 랭크를 증가
    else:
        parent[rb] = ra
        rank[ra] += 1

# 진실을 아는 사람들 합치기
for x in known_lst:
    union(0, x)


parties = []
for _ in range(M):
    party = list(map(int, input().split()))
    # 파티 인원, 파티 인원 리스트
    party_cnt, party_people = party[0], party[1:]
    parties.append(party_people)
    # 파티 참석자는 모두 만난 사람, 합치기
    for i in range(1, party_cnt):
        union(party_people[0], party_people[i])

# 진실을 아는 사람의 리더
truth = find(0)
answer = 0
# 파티 참석자가 진실을 아는 사람의 리더가 아니라면 거짓말 가능
for party in parties:
    if all(find(x) != truth for x in party):
        answer += 1

print(answer)