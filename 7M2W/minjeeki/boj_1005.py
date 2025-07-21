import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 설정 (필요에 따라 조정)
input = sys.stdin.readline

# DFS로 위상 정렬 구현
def dfs(node):
    visited[node] = True  # 현재 노드를 방문 처리
    for next_node in build_near_lst[node]:  # 현재 노드와 연결된 다음 노드 탐색
        if not visited[next_node]:  # 다음 노드를 아직 방문하지 않았다면
            dfs(next_node)
    stack.append(node)  # 현재 노드 처리 완료 후 스택에 추가

T = int(input())  # 테스트 케이스 수

for _ in range(T):
    # N : 건물 수, K : 규칙 수
    N, K = map(int, input().split())
    build_time = [0] + list(map(int, input().split()))  # 각 건물의 건설 시간
    build_near_lst = [[] for _ in range(N + 1)]  # 인접 리스트
    visited = [False] * (N + 1)  # 방문 여부 체크 배열
    stack = []  # 위상 정렬 결과를 저장할 스택
    times = [0] * (N + 1)  # 건물별 완성 시간을 저장할 배열

    # 건물 간 선행 관계 입력
    for _ in range(K):
        x, y = map(int, input().split())
        build_near_lst[x].append(y)

    W = int(input())  # 목표 건물 번호

    # 모든 노드에 대해 DFS 수행
    for i in range(1, N + 1):
        if not visited[i]:  # 아직 방문하지 않은 노드에 대해 DFS 호출
            dfs(i)

    # 스택에서 꺼낸 순서대로 건물 건설 시간 계산
    while stack:
        now = stack.pop()  # 스택에서 노드를 꺼냄
        for next_building in build_near_lst[now]:
            # 현재 건물(now)을 완성한 후 다음 건물(next_building)의 건설 시간을 갱신
            times[next_building] = max(times[next_building], times[now] + build_time[now])

    # 목표 건물 W의 총 건설 시간 출력
    print(times[W] + build_time[W])