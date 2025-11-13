# 1167. 트리의 지름
from collections import deque

# BFS 풀이
def bfs(start):
    visited = [-1] * (V + 1)
    visited[start] = 0
    q = deque([start])

    while q:
        now = q.popleft()
        for nxt, dist in near_list[now]:
            if visited[nxt] == -1:
                visited[nxt] = visited[now] + dist
                q.append(nxt)

    # 가장 먼 노드와 거리 찾기
    far_node = visited.index(max(visited))
    far_dist = max(visited)
    return far_node, far_dist

# 0. 인접 그래프 만들기
V = int(input())
near_list = [[] for _ in range(V + 1)]
for _ in range(V):
    info = list(map(int, input().split()))
    node_a = info[0]
    idx = 1
    while info[idx] != -1:
        node_b, weight = info[idx], info[idx + 1]
        near_list[node_a].append((node_b, weight))
        idx += 2
# 1. 트리는 순환이 없는 구조. 임의의 지점에서 가장 멀리 있는 점은 지름의 끝이라고 볼 수 있다
far_node, far_dist = bfs(1)
# 2. 지름의 끝점에서 가장 먼 지점은 당연히 트리의 지점의 나머지 끝점이 된다.
another_far_node, tree_diameter = bfs(far_node)
print(tree_diameter)