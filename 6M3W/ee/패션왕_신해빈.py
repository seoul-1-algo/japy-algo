import sys
sys.stdin = open('9375.txt')

tc = int(input()) # 테스트 케이스 수

for _ in range(tc):
    n = int(input()) # 해빈이가 가진 의상 수
    
    closet = {}

    for i in range(n):
        cloth, type = input().split()

        closet[type] = closet.get(type, 0) + 1

    answer = 1
    for value in closet.values():
        answer *= value + 1
    
    print(answer - 1)