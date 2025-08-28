import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
n = int(input())
graph = [[] for i in range(n + 1)]
dp = [[0, 0] for i in range(n + 1)]
# dp[u][0] : u가 일반(0)일 때, u 서브트리에서 필요한 얼리어답터 최소 수
# dp[u][1] : u가 얼리어답터(1)일 때, u 서브트리에서 필요한 얼리어답터 최소 수

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for i in range(n + 1)] 
def dfs(start):
    global graph
    global visited
    visited[start] = 1
    if len(graph[start]) == 0:  # 리프 노드가 없으면
        dp[start][1] = 1    # 이 노드를 얼리어답터로 두면 자기 자신만 포함
        dp[start][0] = 0    # 이 노드를 일반으로 두면 얼리어답터가 필요 없음
    else:
        for i in graph[start]:
            if visited[i] == 0:
                dfs(i)  # 아직 방문 안했으면 재귀로 자식 먼저 처리
                dp[start][1] += min(dp[i][0] , dp[i][1])    # start가 얼리어답터일 경우, 자식은 일반/얼리 둘 중 작은쪽
                dp[start][0] += dp[i][1]    # start가 일반이면, 반드시 얼리어답터가 있어야함 -> dp[i][1] 추가
        dp[start][1] += 1   # start 자신을 얼리어답터로 함으로 카운트 1

dfs(1)
print(min(dp[1][0], dp[1][1]))  # 일반/얼리어답터 일 때 더 작은 값이 정답