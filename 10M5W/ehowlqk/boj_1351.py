n, p, q = map(int, input().split())

A = dict()
A[0] = 1

def find_inf_arr(num):
    if num == 0:
        return 1
    
    arr_p = find_inf_arr(num // p) if not A.get(num // p) else A.get(num // p)
    arr_q = find_inf_arr(num // q) if not A.get(num // q) else A.get(num // q)

    A[num] = arr_p + arr_q

    return A[num]

print(find_inf_arr(n))
