import heapq

T = int(input())
for _ in range(T):
    # N : 컴퓨터 개수 / D : 의존성 개수 / C : 해킹당한 컴퓨터 번호
    N, D, C = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    
    for _ in range(D):
        # a : 컴퓨터 번호(to) / b : 의존성 컴퓨터 번호(from) / s : 감염되는데 걸리는 시간
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    # 최단 거리 배열
    INF = float('inf')
    dist = [INF] * (N + 1)
    # 시작점 처리
    dist[C] = 0
    pq = [(0, C)]
    
    while pq:
        current_time, current = heapq.heappop(pq)
        # 이미 처리된 노드라면 무시
        if current_time > dist[current]:
            continue

        # current 노드와 연결된 노드 순회
        for neighbor, weight in graph[current]:
            # 연결된 노드가 감염되기까지 걸리는 시간 계산
            new_time = current_time + weight
            # 연결된 노드가 감염되기까지 걸리는 시간이 기존 시간보다 작다면 업데이트
            if new_time < dist[neighbor]:
                dist[neighbor] = new_time
                # 연결된 노드 heapq에 추가
                heapq.heappush(pq, (new_time, neighbor))
    
    # 감염된 컴퓨터 수와 최대 시간 계산
    infected_count = 0
    max_time = 0
    
    # INF값이 아닌 노드는 감염된 컴퓨터, 해당 컴퓨터가 가진 값은 감염되기까지 걸린 시간
    for i in range(1, N + 1):
        if dist[i] != INF:
            infected_count += 1
            # 감염된 컴퓨터 중 최대 시간 계산
            max_time = max(max_time, dist[i])
    
    print(infected_count, max_time)
