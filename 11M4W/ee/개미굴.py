import sys
sys.stdin = open('14725.txt')

# 트라이의 각 노드는 다음 층의 먹이 정보를 딕셔너리로 저장
class Node():
    def __init__(self):
        self.children = {}

# 주어진 먹이 경로를 트라이에 insert
def insert_path(root, path):
    cur = root # 현재 노드

    for food in path:
        if food not in cur.children:
            cur.children[food] = Node()
        cur = cur.children[food]

# DFS로 탐색해서 개미굴 출력하기
def print_ant_nest(node, depth):
    # 다음 층의 먹이(현재 노드의 자식)
    foods = sorted(node.children.keys())

    for food in foods:
        print(f'{"--" * depth}{food}')

        next_node = node.children[food]
        print_ant_nest(next_node, depth + 1)

# 입력 받기
input = sys.stdin.readline

# 개미굴의 루트 노드
root = Node()

N = int(input()) # 먹이 정보 개수
for _ in range(N):
    K, *path = input().split()
    K = int(K)

    insert_path(root, path)
    
print_ant_nest(root, 0)