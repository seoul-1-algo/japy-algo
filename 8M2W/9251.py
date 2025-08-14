import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

# 이게 생각하기 더 좋다네여(공백넣기)
str1 = " "+str1
str2 = " "+str2

check = [[0 for i in range(len(str2))] for i in range(len(str1))]
N = len(str1)
M = len(str2)

for i in range(N):
    for j in range(M):
        if i == 0 or j == 0 :
            continue
        else:
            if str1[i] == str2[j]:
                check[i][j] = check[i-1][j-1]+1
            else:
                check[i][j] = max(check[i-1][j], check[i][j-1])

print(check[N-1][M-1])