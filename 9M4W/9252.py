first = input()
second = input()

dp = [[0 for i in range(len(second))] for j in range(len(first))]

check = False
for i in range(len(second)):
    if check:
        dp[0][i] +=1
        continue
    if first[0] == second[i]:
        check = True
        dp[0][i] += 1

check = False
for j in range(len(first)):
    if check:
        dp[j][0] +=1
        continue
    if second[0] == first[j]:
        check = True
        dp[j][0] += 1

for i in range(1,len(first)):
    for j in range(1,len(second)):
        if first[i] == second[j]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

# to check lcs string
a,b = len(first)-1, len(second)-1
lcs = []
while a!=0 or b!=0:
    if first[a] == second[b]:
        lcs.append(first[a])
        if a > 0:
            a-=1
        if b > 0:
            b-=1
    else:
        if a > 0 and b > 0:
            if dp[a][b-1] > dp[a-1][b]:
                b-=1
            else:
                a-=1
        elif a == 0:
            b-=1
        elif b == 0:
            a-=1
    

lcs.reverse()
print(dp[len(first)-1][len(second)-1])
if lcs:
    print("".join(lcs))
