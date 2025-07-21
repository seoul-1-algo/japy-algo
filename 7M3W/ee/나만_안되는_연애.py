import sys
sys.stdin = open('14621.txt')

N, M = map(int, input().split()) # 학교의 수 N, 도로의 개수 M

univs = list(input().split()) # 학교 정보
men = set() # 남초 학교
women = set() # 여초 학교

for i in range(N):
    if univs[i] == 'M':
        men.add(i+1)
    else:
        women.add(i+1)

roads = [] # 경로 정보

for _ in range(M):
    u, v, d = map(int, input().split())
    roads.append((d, u, v))

roads.sort() # 거리가 작은 순으로 정렬

# Union-Find

parent = [i for i in range(N+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)

    if x_root < y_root:
        parent[y_root] = x_root
    else:
        parent[x_root] = y_root

# Kruskal

ans = 0
cnt = 0

for d, u, v in roads:
    # 사이클을 생성하지 않으면서, 남초 대학교와 여초 대학교를 연결
    if ((u in men and v in women) or (u in women and v in men)) and find(u) != find(v):
        union(u, v)
        ans += d # 경로 길이
        cnt += 1 # 연결된 대학 수

# 모든 학교가 연결되었는지 체크
if cnt == N-1:
    print(ans)
else:
    print(-1)