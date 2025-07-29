import sys
sys.stdin = open('16282.txt')

n = int(input())
c = 1 # 푸는 고리의 개수

while True:
    if n <= (c + 1) * (2 ** (c + 1) - 1) + c:
        print(c)
        break

    c += 1