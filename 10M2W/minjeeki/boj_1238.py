import heapq

def dijkstra(graph, start, N):
    dist = [float('inf')] * N
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cur_dist, node = heapq.heappop(pq)
        if cur_dist > dist[node]:
            continue
        for next_node, weight in graph[node]:
            new_dist = cur_dist + weight
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
    
    return dist

N, M, X = map(int, input().split())
matrix = [[] for _ in range(N)]
reverse_matrix = [[] for _ in range(N)]
for _ in range(M):
    start_vil, end_vil, move_time = map(int, input().split())
    matrix[start_vil - 1].append((end_vil - 1, move_time))
    reverse_matrix[end_vil - 1].append((start_vil - 1, move_time))

go_x = dijkstra(matrix, X - 1, N)
back_x = dijkstra(reverse_matrix, X - 1, N)

total_dist = [go_x[i] + back_x[i] for i in range(N)]
print(max(total_dist))