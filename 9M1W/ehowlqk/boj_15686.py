import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(n)]

chickens = []

# 치킨집 위치 뽑아내기
for i in range(n):
    for j in range(n):
        if town[i][j] == 2:
            chickens.append((i, j))

# town에서 모든 집을 찾아서 각 치킨집과의 거리 구하기 -> distances에 저장
# distances[집 번호][치킨집 번호] = 집과 치킨집 사이 거리
distances = []
for i in range(n):
    for j in range(n):
        if town[i][j] == 1:
            distances.append([abs(row - i) + abs(col - j) for row, col in chickens])

# combinations로 m개의 치킨집 조합 찾기
cases = list(combinations([idx for idx in range(len(chickens))], m))

answer = 10e9
for case in cases:  # 각 조합을 순회한다.
    # 해당 조합에서의 마을 치킨 거리 초기화
    chicken_distance = 0
    # 각 집을 순회하며 이 조합에서의 치킨거리를 구한다.
    for distance in distances:
        selected = [distance[i] for i in case]  # 선택된 조합의 치킨집들까지의 거리 리스트
        chicken_distance += min(selected)   # 최소 거리를 더한다.
    # 순회가 끝나고 최소 마을 치킨 거리 업데이트
    if chicken_distance < answer:
        answer = chicken_distance

print(answer)
