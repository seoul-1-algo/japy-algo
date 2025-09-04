import sys
from itertools import combinations
input = sys.stdin.readline
N, M = map(int, input().split())
# 치킨집 : M<= <= 13, 집 : 1<= <=13
city = list(list(map(int, input().split())) for _ in range(N))
INF = 10 ** 9
result = INF
# 집 & 치킨집 좌표 저장 리스트
house = []
chicken = []
# 도시 돌면서 치킨집과 집 좌표 저장
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])

# 치킨집 중에서 M개를 고르는 조합 탐색
for chick in combinations(chicken, M):
    temp = 0    # 현재 조합에서 가장 가까운 치킨집과의 거리
    for i in house:
        length = 999    # 이 집에서 치;킨집까지 최소 거리
        for j in range(M):  
            # 치킨 거리 = |집의 행 - 치킨집 행| + |집의 열 - 치킨집의 열|
            length = min(length, abs(i[0] - chick[j][0]) + abs(i[1] - chick[j][1]))
        temp += length
    
    result = min(result, temp)

print(result)