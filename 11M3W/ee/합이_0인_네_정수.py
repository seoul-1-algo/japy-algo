import sys
sys.stdin = open('7453.txt')

input = sys.stdin.readline

n = int(input()) # 배열의 크기

# 네 개의 배열에 나눠 담기
A, B, C, D = [], [], [], []

for i in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

# A + B, C + D를 담는 배열
AB, CD = [], []
for i in range(n):
    for j in range(n):
        AB.append(A[i] + B[j])
        CD.append(C[i] + D[j])

ans = 0 # 합이 0이 되는 쌍의 개수를 담을 변수

AB.sort()
CD.sort()

K = len(AB) # AB, CD의 배열 길이

i = 0
j = K - 1

while i < K and j >= 0:
    tmp = AB[i] + CD[j]

    if tmp == 0: # A + B + C + D = 0
        
        # AB배열에서 AB[i] 값이 몇 개 들어있는지 세기
        valAB = AB[i]
        cntAB = 0
        
        while i < K and AB[i] == valAB:
            cntAB += 1
            i += 1
        
        # CD배열에서 CD[j] 값이 몇 개 들어있는지 세기
        valCD = CD[j]
        cntCD = 0

        while j >= 0 and CD[j] == valCD:
            cntCD += 1
            j -= 1
        
        ans += cntAB * cntCD # ++두 값의 곱

    elif tmp < 0: # 합이 0보다 작으면
        i += 1 # AB 값을 키운다

    else: # 합이 0보다 크면
        j -= 1 # CD 값을 줄인다


# # AB + CD = 0를 만족하는,
# # 즉, AB = -CD인 값을 이분탐색으로 찾기
# AB.sort()

# for val in CD:
#     target = -val

#     start = 0
#     end = 

#     while start <= end:
#         mid = (start + end) // 2

#         if AB[mid] == target:
#             ans += 1
#             break
#         elif AB[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1

print(ans)