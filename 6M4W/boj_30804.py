N = int(input())
tanghuru = list(map(int, input().split()))
start_p, end_p = 0, 0
type_num = 1
max_len = 1
fruit_num = [0] * 10  # 1~9까지 OK
fruit_num[tanghuru[0]] = 1

while end_p < N - 1:
    if type_num <= 2:
        end_p += 1
        cur_fruit = tanghuru[end_p]
        if fruit_num[cur_fruit] == 0:
            type_num += 1
        fruit_num[cur_fruit] += 1
        if type_num <= 2:
            max_len = max(max_len, end_p - start_p + 1)
    else:
        delete_fruit = tanghuru[start_p]
        fruit_num[delete_fruit] -= 1
        if fruit_num[delete_fruit] == 0:
            type_num -= 1
        start_p += 1
print(max_len)
