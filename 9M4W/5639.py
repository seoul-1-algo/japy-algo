import sys
sys.setrecursionlimit(10**6)

nums = []

while True:
    try:
        nums.append(int(input()))
    except:
        break

def orders(arr):
    if not arr:
        return
    
    left, right = [], []
    mid = arr[0]

    for i in range(1,len(arr)):
        if arr[i] > mid:
            left = arr[1:i]
            right = arr[i:]
            break
    
    else:
        left = arr[1:]
    
    orders(left)
    orders(right)
    print(mid)

orders(nums)
