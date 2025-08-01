n = int(input())
ans = 1
while (n > (ans+1)*2**(ans+1)-1):
    ans += 1

print(ans)
