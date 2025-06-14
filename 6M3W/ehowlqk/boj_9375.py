T = int(input())
for _ in range(T):
    n = int(input())
    closet = dict()

    for __ in range(n):
        cloth, category = input().split()
        # 이미 등록된 카테고리: 기존 배열에 append
        if closet.get(category):
            closet[category].append(cloth)
        # 새로 등록된 카테고리: 새로운 배열에 담아 등록
        else:
            closet[category] = [cloth]

    answer = 1

    for key in closet:
        # 경우의 수 구하기: <종류 별 의상 개수 + 1>을 모두 곱한다(+1은 착용하지 않는 경우)
        answer *= len(closet[key]) + 1

    print(answer - 1)
