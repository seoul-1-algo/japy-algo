import sys

input = sys.stdin.readline
SIZE = 2**20

N = int(input())
N_range = range(N)

A, B, C, D = [0]*N, [0]*N, [0]*N, [0]*N
for i in N_range:
    A[i], B[i], C[i], D[i] = map(int, input().split())
    C[i] = -C[i]
    D[i] = -D[i]

A.sort(), B.sort(), C.sort(), D.sort()

RB, RD = [0]*N, [0]*N
LK, CNTS = [0]*SIZE, [0]*SIZE

LM = min(A[0]+B[0], C[0]+D[0])+SIZE-1
AB, CD, OK, ANS = 0, 0, 0, 0

while AB < N and CD < N:
    OK += 1

    # A+B 확인
    for i in range(AB, N):
        L = LM-A[i]
        while RB[i] < N:
            S = L-B[RB[i]]
            if S < 0: break
            
            # key와 count 갱신
            if LK[S] == OK:
                CNTS[S] += 1
            else:
                LK[S] = OK
                CNTS[S] = 1

            RB[i] += 1

            if RB[i] == N: AB += 1
    
    # C+D 확인
    for i in range(CD, N):
        L = LM-C[i]
        while RD[i] < N:
            S = L-D[RD[i]]
            if S < 0: break

            if LK[S] == OK: ANS += CNTS[S]
            RD[i] += 1
            if RD[i] == N: CD += 1
    
    LM += SIZE

print(ANS)
    



    # i = AB
    # while i < N and TB[i] < LM:
    #     L = LM - A[i]
    #     r = RB[i]
    #     while r < N:
    #         S = L - B[r]
    #         if S < 0:
    #             break
    #         if LK[S] == OK:
    #             CNTS[S] += 1
    #         else:
    #             LK[S] = OK
    #             CNTS[S] = 1
    #         r += 1
    #     RB[i] = r
    #     if r == N:
    #         AB = i + 1
    #     i += 1
    
    # # TB[i] >= LM인 행 확인
    # i = AB
    # while i < N:
    #     L = LM - A[i]
    #     r = RB[i]
    #     while r < N:
    #         S = L - B[r]
    #         if S < 0:
    #             break
    #         if LK[S] == OK:
    #             CNTS[S] += 1
    #         else:
    #             LK[S] = OK
    #             CNTS[S] = 1
    #         r += 1
    #     RB[i] = r
    #     if r == N:
    #         AB = i + 1
    #     i += 1

    # # C+D 확인
    # i = CD
    # while i < N and TD[i] < LM:
    #     L = LM - C[i]
    #     r = RD[i]
    #     while r < N:
    #         S = L - D[r]
    #         if S < 0:
    #             break
    #         if LK[S] == OK:
    #             ANS += CNTS[S]
    #         r += 1
    #     RD[i] = r
    #     if r == N:
    #         CD = i + 1
    #     i += 1
    
    # # TD[i] >= LM인 행 확인
    # i = CD
    # while i < N:
    #     L = LM - C[i]
    #     r = RD[i]
    #     while r < N:
    #         S = L - D[r]
    #         if S < 0:
    #             break
    #         if LK[S] == OK:
    #             ANS += CNTS[S]
    #         r += 1
    #     RD[i] = r
    #     if r == N:
    #         CD = i + 1
    #     i += 1    

    # LM += SIZE

# print(ANS)
