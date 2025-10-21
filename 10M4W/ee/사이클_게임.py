import sys
sys.stdin = open('20040.txt')

# Union-Find
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)

    # 같은 루트라면? 이미 같은 집합에 있음 => 사이클 발생!
    if a == b:
        return True
    
    # 다르면 합친다
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

    return False    

# 입력 받기
n, m = map(int, input().split())

parent = [i for i in range(n)]

for turn in range(1, m+1):
    a, b = map(int, input().split())

    if union(a, b): # 사이클이 존재하면
        print(turn) # 몇 번째 차례인지 출력
        break
else:
    print(0)

