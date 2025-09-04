import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int,input().split())
viliage = []
house = []
chicken = []
for i in range(n):
    viliage.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if viliage[i][j] == 1:
            house.append([i,j])
        if viliage[i][j] == 2:
            chicken.append([i,j])

all = list(combinations(chicken,m))
min_chicken_length = 100000

for now_combination in all:
    temp_city_length = 0
    for now_home in house:
        temp_chicken_length = 10000
        for now_chicken in now_combination:
            temp_chicken_length = min(temp_chicken_length,abs(now_home[0]-now_chicken[0])+abs(now_home[1]-now_chicken[1]))
        temp_city_length+=temp_chicken_length
    min_chicken_length = min(min_chicken_length,temp_city_length)

print(min_chicken_length)
