import sys
sys.stdin = open('30804.txt')

N = int(input()) # 과일의 개수
fruits = list(map(int, input().split())) # 처음 탕후루

start = 0
end = 0

max_count = 0
count = 0

fruit_cnt = [0] * 10 # (1 <= Si <= 9)
fruit_set = set()

while end < N:
    if len(fruit_set) >= 2 and fruits[end] not in fruit_set: # 뒤쪽 과일을 넣으면 3개가 된다면?
        fruit_cnt[fruits[start]] -= 1
        count -= 1 


        if fruit_cnt[fruits[start]] == 0: # 앞쪽 과일 종류가 다 빠졌다면
            fruit_set.remove(fruits[start])
        
        start += 1 # 앞에껄 뺀다
    else: # 뒤쪽 과일을 넣어도 3개가 안 됨

        if fruit_cnt[fruits[end]] == 0: # 뒤쪽 과일을 처음 넣으면
            fruit_set.add(fruits[end]) # set에 추가

        fruit_cnt[fruits[end]] += 1 # 과일 갯수 카운트
        count += 1
        end += 1

    if count > max_count:
        max_count = count

    
print(max_count)