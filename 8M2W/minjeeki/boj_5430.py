# 골드 5 / 5430 AC / 메모리 : 40740KB, 시간 : 272ms

from collections import deque

T = int(input())       # T (테스트케이스) <= 100
for _ in range(T):     # p 길이 합, n 길이 합은 70만 넘지 않음
    p = input()        # 1 <= p (수행할 함수, R 또는 D) < 100,000
    n = int(input())   # 0 <= n (배열에 들어있는 수의 개수) <= 100,000
    arr = input()
    if arr == '[]':
        num_deq = deque()
    else:
        num_deq = deque(map(int, arr[1:-1].split(',')))  # 배열 정수, 1 <= x (배열 요소) <= 100

    is_direction_right = True
    is_error = False
    for _funct in p:
        if _funct == 'R' and is_direction_right:
            is_direction_right = False
        elif _funct == 'R' and not is_direction_right:
            is_direction_right = True
        elif _funct == 'D' and n > 0:
            if is_direction_right:
                num_deq.popleft()
                n -= 1
            else:
                num_deq.pop()
                n -= 1
        elif _funct == 'D' and n == 0:
            is_error = True
            break
    if is_error:
        print("error")
    else:
        if is_direction_right:
            result = list(num_deq)
        else:
            result = list(num_deq)[::-1]
        print('[' + ','.join(map(str, result)) + ']')