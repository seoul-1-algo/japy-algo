import sys
sys.setrecursionlimit(10**6)

input = open('boj_1167.txt', 'r').readline
# input = sys.stdin.readline

def find_furthest(start, edges, v):
    visited = [False] * (v+1)
    visited[start] = True
    def bfs(node, cost):
        result = (node, cost)
        # print("visited:", node)
        for nxt, dist in edges[node]:
            if not visited[nxt]:
                # print("edges:", nxt, dist)
                visited[nxt] = True
                tmp = bfs(nxt, cost + dist)
                if tmp[1] > result[1]:
                    result = tmp
                visited[nxt] = False
        
        return result
    
    return bfs(start, 0)


v = int(input())

edges = [list() for _ in range(v+1)]

for _ in range(v):
    lst = list(map(int, input().split()))

    node = lst[0]
    for i in range(len(lst) // 2 - 1):
        edges[node].append((lst[2*i + 1], lst[2*i + 2]))

EoD = find_furthest(1, edges, v)[0]
print(find_furthest(EoD, edges, v)[1])



    



"""
2n + 1
2n+1, 2n+2

"""