n, m = map(int, input().split())
who_knows_truth = list(map(int, input().split()))

# 진실을 아는 사람이 없다면: 전부 구라 가능
if len(who_knows_truth) == 1:
    print(m)
else:
    edges = [set() for _ in range(n + 1)]      # 간선(같은 파티에 참석)
    parties = [list(map(int, input().split())) for _ in range(m)]       # 파티 정보
    # 같은 파티에 참가한 사람을 간선으로 언결
    for party in parties:
        for i in range(1, len(party)):
            for j in range(i, len(party)):
                if i != j:
                    edges[party[i]].add(party[j])
                    edges[party[j]].add(party[i])

    # 스택에 진실을 아는 사람들 추가
    stack = [who_knows_truth[people] for people in range(1, who_knows_truth[0] + 1)]
    visited = [False] * (n + 1)      # visited: 방문처리 + True일 경우 이 사람이 포함된 파티에서는 거짓말 X
    for i in stack:
        visited[i] = True
    while stack:
        cannot_lie = stack.pop()

        # 같은 파티에 참가한 사람들 모두 거짓말 X -> visited에 처리한다.
        for neighbour in edges[cannot_lie]:
            if not visited[neighbour]:
                stack.append(neighbour)
                visited[neighbour] = True

    answer = 0
    for party in parties:
        for people in party[1:]:
            # 진실 파티에 참가한 사람이 있다면 break
            if visited[people]:
                break
        # 진실 파티에 참가한 사람이 없다면 거짓파티 수++
        else:
            answer += 1

    print(answer)
