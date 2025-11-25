# input = open('1091.txt', 'r').readline

N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))
arr = [x for x in range(N)]
init = [x for x in range(N)]

answer = 0

while (1):
    # 확인하기
    success = True
    for i in range(N):
        if i % 3 != P[arr[i]]:
            success = False
    if success:
        print(answer)
        break

    tmp = [-1] * N
    for i in range(N):
        tmp[S[i]] = arr[i]

    arr = tmp
    answer += 1
    
    if arr == init:
        # print(arr, S)
        answer = -1
        print(answer)
        break
