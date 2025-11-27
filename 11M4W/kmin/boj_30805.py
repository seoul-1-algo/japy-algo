import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

commen_elements = set(A) & set(B)   # A배열과 B배열의 교집합 찾기

if not commen_elements:
    print(0)
    exit()

result = []
while commen_elements:
    max_val = max(commen_elements)  # 공통에 있는 숫자들 중 에서 제일 큰 거부터 하나
    result.append(max_val)

    idx1 = A.index(max_val) # 뽑은 큰값의 A의 인덱스를 찾기
    idx2 = B.index(max_val) # 뽑은 큰 값의 B의 인덱스를 찾기
    A = A[idx1 + 1:]    # 최대 값 다음부터
    B = B[idx2 + 1:]    # 최대 값 다음부터

    commen_elements = set(A) & set(B)   # A와 B의 공통 큰값 이후만 남았으므로 공통요소 업데이트

print(len(result))
print(*result)