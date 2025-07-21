N = int(input())
M = int(input())
S = input()

total = 0
s_idx = 0
cnt = 0

while s_idx <= M - 2:
    if S[s_idx] == 'I':
        e_idx = s_idx
        cnt = 0

        while e_idx + 2 < M and S[e_idx + 1] == 'O' and S[e_idx + 2] == 'I':
            cnt += 1
            e_idx += 2

            if cnt == N:
                total += 1

                if e_idx + 2 < M and S[e_idx + 1] == 'O' and S[e_idx + 2] == 'I':
                    s_idx += 2
                    cnt -= 1
                else:
                    break
        s_idx = e_idx + 1

    else:
        s_idx += 1

print(total)