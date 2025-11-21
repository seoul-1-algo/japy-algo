import sys
input = sys.stdin.readline
n = int(input())
A = []
B = []
C = []
D = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
AB = [] # A+B 합
CD = [] # C+D 합
for i in range(n):
    for j in range(n):
        AB.append(A[i] + B[j])
        CD.append(C[i] +D[j])
AB.sort()
CD.sort()

result = 0
start = 0           # AB는 작은거부터
end = len(CD) - 1   # CD는 큰거부터

while start < len(AB) and end >= 0: # AB + CD = 0 찾기
    if AB[start] + CD[end] == 0:
        ab_value = AB[start]    # A+B의 값이 같은 경우의 수 찾기 위해서
        cd_value = CD[end]
        ab_count = 0    # A+B의 값이 같은 경우
        cd_count = 0
        while start < len(AB) and AB[start] == ab_value:
            start += 1  # 값이 중복되는게 있으니깐, 확인될때마다 start 추가
            ab_count += 1
        while end >= 0 and CD[end] == cd_value:
            end -= 1
            cd_count += 1
        result += ab_count * cd_count
        

    
    elif AB[start] + CD[end] > 0:
        end -= 1
    else:
        start += 1


print(result)