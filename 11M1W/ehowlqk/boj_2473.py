import sys
# input = sys.stdin.readline
input = open('boj_2473.txt', 'r').readline
n = int(input())
arr = list(map(int, input().split()))

def solve(n, arr):
    arr.sort()
    max_pH = float('inf')
    answer = []

    for i in range(n-2):
        start, end = i+1, n-1
        base = arr[i]
        while start < end:            
            pH = base + arr[start] + arr[end]
            if abs(pH) < max_pH:
                max_pH = abs(pH)
                answer = [base, arr[start], arr[end]]
            
            if pH < 0:
                start += 1
            elif pH > 0:
                end -= 1
            else:
                return answer
            
    return answer

print(*solve(n, arr))
