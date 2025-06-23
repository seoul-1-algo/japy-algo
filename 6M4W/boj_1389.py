N, M = map(int, input().split())
big_num = N ** N
distance = [[big_num] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
	distance[i][i] = 0
for _ in range(M):
	A, B = map(int, input().split())
	distance[A][B] = 1
	distance[B][A] = 1
	
for k in range(1, N + 1):
	for i in range(1, N + 1):
		for j in range(i + 1, N + 1):
			distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
			distance[j][i] = distance[i][j]

min_bacon, winner = big_num, 0
for i in range(1, N + 1):
	bacon = sum(distance[i]) - distance[i][0]
	if min_bacon > bacon:
		min_bacon = bacon
		winner = i
print(winner)
