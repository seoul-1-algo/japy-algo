n = int(input())
tanghuru = list(map(int, input().split()))

start, end = 0, 1
answer = 1
fruits = {tanghuru[0]: 1}   # 과일 종류별 개수

while end < n:
    # 과일 두 개 이하로 만들었을 때:
    if len(fruits) < 3:
        fruits[tanghuru[end]] = fruits.get(tanghuru[end], 0) + 1    # 딕셔너리에 추가
        end += 1    # end 증가
        answer = max(answer, end - start) if len(fruits) < 3 else answer    # end 증가 후 과일 종류가 2개 이하일 때만 최대 길이 갱신

    else:
        if fruits[tanghuru[start]] == 1:    # start의 과일이 한 개 뿐일 때: 딕셔너리에서 제거
            fruits.pop(tanghuru[start])
        else:
            fruits[tanghuru[start]] -= 1    # 그 외: 개수 -1만큼 감소
        start += 1  # start 증가

print(answer)
