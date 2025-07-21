n = int(input())

fruit = list(map(int, input().split()))

start = 0
end = n-1
permutation = []

for i in range(9,0,-1):
    for j in range(i,0,-1):
        if i == j:
            continue
        else:
            permutation.append([i,j])

check = []
for now in permutation:
    cnts = []
    cnt = 0
    for each in fruit:
        if each in now:
            cnt += 1
        else:
            cnts.append(cnt)
            cnt = 0
    if cnt != 0:
        cnts.append(cnt)
    check.append(max(cnts))

print(max(check))