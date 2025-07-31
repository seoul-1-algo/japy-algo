import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
def dslr(n, command):   # dslr 구현
    if command == "D":
        return (n * 2) % 10000
    if command == "S":
        return (n - 1) % 10000
    if command == "L":
        return (10 * n + (n // 1000)) % 10000
    if command == "R":
        return (((n % 10) * 1000) + (n // 10)) % 10000

def bfs(n):
    q = deque()
    q.append((n, ""))   # 시작 숫자와 문자열 초기값 ""을 큐에 넣음
    visited[n] = True

    while q:
        n, result = q.popleft()

        if n == b:  # 목표 숫자 b에 도달했으면 명령어 반환
            return result
        for command in commands:    # 명령어 d,s,l,r 4개 순회
            newNum = dslr(n, command)   # 명령어를 적용한 결과 숫자
            if not visited[newNum]:
                visited[newNum] = True
                q.append((newNum, result + command))

commands = ["D", "S", "L", "R"]
for _ in range(T):
    a, b = map(int, input().split())
    visited = [False] * 10000
    print(bfs(a))

