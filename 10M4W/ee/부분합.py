import sys
sys.stdin = open('1806.txt')

N, S = map(int, input().split())
arr = list(map(int, input().split())) # 수열

INF = 1e20

ans = INF 

s = 0
e = 1

temp = arr[s]

while e <= N:
    if temp < S: 
        if e == N:
            break
        temp += arr[e]
        e += 1
    else:
        ans = min(ans, e - s)
        temp -= arr[s]
        s += 1

print(ans if ans != INF else 0)