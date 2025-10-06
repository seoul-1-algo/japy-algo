import sys
sys.stdin = open('2467.txt')

N = int(input()) 
liquids = list(map(int, input().split())) # 용액

front = 0
rear = N-1

min_val = 1e12
ans = [front, rear]

while front < rear:
    temp = liquids[front] + liquids[rear]

    if min_val >= abs(temp):
        min_val = abs(temp)
        ans = [front, rear]

    if temp > 0:
        rear -= 1
    elif temp < 0:
        front += 1
    else:
        break

print(liquids[ans[0]], liquids[ans[1]])
