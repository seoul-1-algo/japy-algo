import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    clothes = {}        # 종류, 갯수 딕셔네리 생성
    n = int(input())
    for _ in range(n):
        name, type = input().split()
        if type in clothes:
            clothes[type] += 1  # 해당 종류가 존재하면 갯수 + 1
        else:
            clothes[type] = 1   # 해당 종류가 존재하지 않으면 갯수 - 1
    
    answer = 1                  # 정답 초기 설정 1로 설정
    for i in clothes:
        answer *= (clothes[i] + 1)     # 딕셔너리 순회하며 갯수 + 1(안입은 경우) 곱함
    
    answer -= 1     # 발가벗었을 때 제외
    print(answer)

    
