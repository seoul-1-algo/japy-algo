import sys
sys.stdin = open('1644.txt')

N = int(input())

# '에라토스테네스의 체' 방식으로 N 이하의 소수 구하기

sieve = [True] * (N+1) # 처음엔 모든 수가 다 소수(True)라고 가정하고 시작 !!

sieve[0] = False # 0은 소수가 아님
sieve[1] = False # 1도 소수가 아님

for i in range(2, int(N**0.5) + 1): # 제곱근까지만 검사한다
    if sieve[i]:
        for j in range(i*i, N+1, i): # i의 배수 제거
            sieve[j] = False

primes = []

for idx, is_prime in enumerate(sieve):
    if is_prime:
        primes.append(idx)

left = 0
right = 0

cur_sum = 0 # 현재 합
cnt = 0 # 경우의 수

while True:
    # 종료 조건
    if right == len(primes) and cur_sum < N:
        break

    # 합이 N보다 크거나 같으면 왼쪽 포인터 이동
    if cur_sum >= N:
        if cur_sum == N: # 같으면 카운터 증가
            cnt += 1
        cur_sum -= primes[left]
        left += 1

    # 합이 아직 작고, 오른쪽으로 옮길 수 있으면
    else:
        cur_sum += primes[right]
        right += 1
    
print(cnt)