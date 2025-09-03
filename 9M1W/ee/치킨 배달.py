import sys
sys.stdin = open('15686.txt')

from itertools import combinations

N, M = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(N)] # 도시의 정보

houses = []
chickens = []

for i in range(N):
    for j in range(N):
        if cities[i][j] == 1: # 집
            houses.append((i, j))
        elif cities[i][j] == 2: # 치킨집
            chickens.append((i, j))

distances = [[0] * len(chickens) for _ in range(len(houses))]
for h_idx, (hr, hc) in enumerate(houses):
    for c_idx, (cr, cc) in enumerate(chickens):
        distances[h_idx][c_idx] = abs(hr - cr) + abs(hc - cc)

ans = 1e9
for combination in combinations(range(len(chickens)), M):
    chicken_distance = 0

    for h in range(len(houses)):
        candidates = []
        for k in combination:
            candidates.append(distances[h][k])
        min_distance = min(candidates)

        chicken_distance += min_distance

        if chicken_distance >= ans:
            break
    
    if chicken_distance < ans:
        ans = chicken_distance

print(ans)
