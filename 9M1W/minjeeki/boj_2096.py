N = int(input())
LINE_NUM = 3

a, b, c = map(int, input().split())
min_arr = [a, b, c]
max_arr = [a, b, c]

for i in range(N - 1):
    pmin_a, pmin_b, pmin_c = min_arr
    pmax_a, pmax_b, pmax_c = max_arr
    new_a, new_b, new_c = map(int, input().split())

    min_arr[0] = min(pmin_a, pmin_b) + new_a
    min_arr[1] = min(pmin_a, pmin_b, pmin_c) + new_b
    min_arr[2] = min(pmin_b, pmin_c) + new_c
    max_arr[0] = max(pmax_a, pmax_b) + new_a
    max_arr[1] = max(pmax_a, pmax_b, pmax_c) + new_b
    max_arr[2] = max(pmax_b, pmax_c) + new_c

print(max(max_arr), min(min_arr))
