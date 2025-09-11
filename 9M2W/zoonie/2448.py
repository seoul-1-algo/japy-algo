n = int(input())

arr = [[" " for _ in range(2*n-1)]for _ in range(n)]
y = n
y /= 3
x = 0
while True:
    if y==1:
        break
    y/=2
    x+=1

#별 찍기
def star(exponent, x,y):
    if exponent == 0:
        arr[x][y] = "*"
        arr[x+1][y-1] = "*"
        arr[x+1][y+1] = "*"
        for i in range(5):
            arr[x+2][y-2+i] = "*"
        return
    else:
        star(exponent-1, x,y)
        star(exponent-1, x+3*2**(exponent-1),y-3*2**(exponent-1))
        star(exponent-1, x+3*2**(exponent-1),y+3*2**(exponent-1))

star(x,0,n-1)
for i in range(n):
    print("".join(arr[i]))