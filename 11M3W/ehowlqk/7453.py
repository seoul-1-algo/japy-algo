import sys

# input = open('7453.txt', 'r').readline
input = sys.stdin.readline

n = int(input())
N_range = range(n)

A, B, C, D = [], [], [], []
A_add = A.append
B_add = B.append
C_add = C.append
D_add = D.append

for _ in N_range:
    a, b, c, d = map(int, input().split())
    A_add(a)
    B_add(b)
    C_add(c)
    D_add(d)

size = n * n
AB = [0] * size
CD = [0] * size

A_local = A
B_local = B
C_local = C
D_local = D

idx = 0
for i in N_range:
    a = A_local[i]
    c = C_local[i]
    for j in N_range:
        AB[idx] = a + B_local[j]
        CD[idx] = c + D_local[j]
        idx += 1

AB.sort()
CD.sort()
answer = 0

AB_local = AB
CD_local = CD
lenAB = len(AB_local)
lenCD = len(CD_local)

start = 0
end = lenCD - 1

while start < lenAB and 0 <= end:
    vAB = AB_local[start]
    vCD = CD_local[end]
    _sum = vAB + vCD
    if _sum == 0:
        start_nxt, end_nxt = start+1, end-1
        while start_nxt < lenAB and vAB == AB_local[start_nxt]: 
            start_nxt += 1
        while end_nxt >= 0 and vCD == CD_local[end_nxt]: 
            end_nxt -= 1
        answer += (start_nxt - start) * (end - end_nxt)
        start = start_nxt
        end = end_nxt
    elif _sum < 0:
        start += 1
    else:
        end -= 1

print(answer)
