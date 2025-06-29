import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
ans = 0
left = 0    # 왼쪽 포인터
count = {}  # 과일 종류별 갯수
type_count = 0  # 현재 과일 종류 갯수
for i in range(N):  # 오른쪽 포인터 i를 하나씩 오른쪽으로 이동
    if arr[i] in count:
        count[arr[i]] += 1  # 이미 있는 종류면 + 1
    else:
        count[arr[i]] = 1   # 새로운 종류면 1
        type_count += 1     # 과일 종류 + 1
    while type_count > 2:   # 종류가 2개 초과
        count[arr[left]] -= 1   # 왼쪽에서 1개 제거
        if count[arr[left]] == 0:   # 해당 과일의 갯수 0되면 삭제
            del count[arr[left]]
            type_count -= 1     # 과일 종류 - 1
        left += 1   # 왼쪽 포인터 + 1

    ans = max(ans, i - left + 1)

print(ans)