# 골드 5 2467 용액

N = int(input())
vals = list(map(int, input().split()))

idx_minus = 0
idx_plus = N - 1

best_abs = float('inf')
ans_left, ans_right = vals[idx_minus], vals[idx_plus]


while idx_minus < idx_plus:
    s = vals[idx_minus] + vals[idx_plus]
    if abs(s) < best_abs:
        best_abs = abs(s)
        ans_left, ans_right = vals[idx_minus], vals[idx_plus]
        if best_abs == 0:
            break

    if s < 0:
        idx_minus += 1
    else:
        idx_plus -= 1

print(ans_left, ans_right)