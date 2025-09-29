import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

arr = []

while True:
    try:
        arr.append(int(input()))
    except:
        break


def gndnl(start, end):
    if start >= end:
        return
    
    mid = end
    for i in range(start + 1, end):
        if arr[i] > arr[start]:
            mid = i
            break
    
    gndnl(start + 1, mid)
    gndnl(mid, end)
    print(arr[start])

    return

gndnl(0, len(arr))