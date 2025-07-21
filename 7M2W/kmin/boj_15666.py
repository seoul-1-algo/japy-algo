import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()  # 오름차순 정렬
ans = []    # 최종 정답
def back(n, s, tlst):   # n : 현재 수열 길이, s : 탐색시작할 인덱스, tlst : 현재까지 만든 수열
    if n == M:  # 수열의 길이가 M이라면 정답에 추가
        ans.append(tlst)
        return
    prev = 0    # 중복된 숫자 사용 방지, 현재 깊이에서 직전에 사용한 숫자를 기록
    for j in range(s, N):
        if prev != arr[j]:  # 중복되지 않았다면
            prev = arr[j]   # 현재 숫자를 prev에ㅓ 저장해 다음 루프에서 중복인지 비교
            back(n+1, j, tlst + [arr[j]])   # j를 그대로 넘겨 같은 숫자도 여러번 선택 가능


back(0, 0, [])
for lst in ans:
    print(*lst)