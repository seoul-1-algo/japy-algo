# input = open('30805.txt', 'r').readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))


# 구간 내 최대 공통값 찾기
def find(idx1, idx2):
    max_num = 0
    ri1, ri2 = idx1, idx2
    for i in range(idx1, M):
        if max_num < B[i]:
            for j in range(idx2, N):
                if A[j] == B[i]:
                    max_num = B[i]
                    ri1, ri2 = i, j
                    break
                    
    return [ri1+1, ri2+1, max_num]


max_num = 0
idx1, idx2 = 0, 0
answer = []

while idx1 < M and idx2 < N:
    idx1, idx2, added = find(idx1, idx2)
    if added: answer.append(added)

K = len(answer)
print(K)
if K:
    print(*answer)
