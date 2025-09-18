import sys
input = sys.stdin.readline

# 9251 lcs
a = list(input())   
b = list(input())

lcs = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

# 여기서부터 9252 추가
# 주의: a, b의 마지막에는 '\n'이 들어있을 수 있다.
# 우리는 LCS 문자열에 엔터('\n')가 섞임
# 역추적을 시작할 (i, j) 위치를 '\n'을 제외
i = len(a)  # DP 테이블의 세로 인덱스 시작점 (a 쪽 길이)
j = len(b)  # DP 테이블의 가로 인덱스 시작점 (b 쪽 길이)

# 만약 a의 마지막 문자가 '\n'이라면, 그 문자는 무시하고 한 칸 앞에서 시작
if i > 0 and a[-1] == '\n':
    i -= 1
# b도 동일 처리
if j > 0 and b[-1] == '\n':
    j -= 1

# 역추적 결과 담을 리스트(뒤에서부터)
ans = []

# - a[i-1] == b[j-1]라면, 이 문자는 LCS의 '마지막 글자' 중 하나이므로 ans에 담고 대각선으로 이동(i-1, j-1)
# - 다르면, 위(lcs[i-1][j])와 왼(lcs[i][j-1]) 중 더 큰 값 쪽으로 이동
while i > 0 and j > 0:
    if a[i - 1] == b[j - 1]:
        # 공통 문자를 찾았으니 결과에 추가
        ans.append(a[i - 1])
        # lcs에 포함시켰으니, 두 문자열 모두 한 글자씩 뒤로 이동
        i -= 1
        j -= 1
    else:
        # 위쪽과 왼쪽 중 DP 값이 큰 쪽으로 이동 (더 긴 LCS가 있었던 방향)
        if lcs[i - 1][j] >= lcs[i][j - 1]:
            i -= 1
        else:
            j -= 1

# ans는 역순으로 받았으니, 리버스
ans.reverse()

lcs_str = ''.join(ans)


print(len(lcs_str))
print(lcs_str)
