import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    n = int(input())
    combination = {}
    for i in range(n):
        clotes_name, clothes_type = map(str, input().strip().split())
        if clothes_type in list(combination.keys()):
            combination[clothes_type]+=1
        else:
            combination[clothes_type]=1
    num = 1
    for now_type in list(combination.keys()):
        num*=(combination[now_type]+1)
    print(num-1)