n = int(input())
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

# 전체를 순회하며 돌면 시간초과가 발생하기 때문에 묶어서 처리한다.
AB = []
for a in A:
    for b in B:
        AB.append(a + b)
AB.sort()

CD = []
for c in C:
    for d in D:
        CD.append(c + d)
CD.sort()

answer = 0
left, right = 0, len(CD) - 1
# 투 포인터 알고리즘을 사용하여 두 배열을 순회하며 합이 0인 경우를 찾는다.
while 0 <= right and left < len(AB):
    cur_sum = AB[left] + CD[right]
    if cur_sum < 0:
        left += 1
    elif cur_sum > 0:
        right -= 1
    else:
        # AB[left]와 같은 값이 연속으로 몇 개 있는지 센다
        ab_count = 1
        ab_idx = left + 1
        while ab_idx < len(AB) and AB[ab_idx] == AB[left]:
            ab_count += 1
            ab_idx += 1
        
        # CD[right]와 같은 값이 연속으로 몇 개 있는지 센다
        cd_count = 1
        cd_idx = right - 1
        while cd_idx >= 0 and CD[cd_idx] == CD[right]:
            cd_count += 1
            cd_idx -= 1
        
        # 두 개수를 곱해서 answer에 더한다
        answer += ab_count * cd_count
        left = ab_idx
        right = cd_idx

print(answer)
