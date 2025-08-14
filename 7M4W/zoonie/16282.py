t = int(input())
n = 0
while True:
    if 2**(n+1)*(n+1) -1 >= t:
        print(n)
        break
    else:
        n+=1