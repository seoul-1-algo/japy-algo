import sys
sys.stdin = open('30805.txt')

N = int(input()) # 수열 A의 길이
A = list(map(int, input().split()))
M = int(input()) # 수열 B의 길이
B = list(map(int, input().split()))

i, j = 0, 0
ans = []

while True:
    # A, B 수열이 공통으로 가지고 있는 수의 집합
    commons = set(A[i:]) & set(B[j:])

    # 종료 조건
    if not commons:
        break

    # 현재 구간에서 공통 값들 중 max 값
    # 이 값이 다음 원소가 되면 사전 순 최대 !!
    max_val = max(commons)

    # 수열에서 max_val 값이 처음으로 등장하는 위치 찾기
    ni = i
    while ni < N:
        if A[ni] == max_val:
            break
        ni += 1
    
    nj = j
    while nj < M:
        if B[nj] == max_val:
            break
        nj += 1
        
    # 정답 리스트에 추가
    ans.append(max_val)

    # 인덱스 업데이트
    i = ni + 1
    j = nj + 1

print(len(ans))
if ans:
    print(*ans)