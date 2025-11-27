# input = open('14725.txt', 'r').readline

N = int(input())
trie = {}
for _ in range(N):
    K, *lst = input().split()
    tmp = trie
    for level in lst:
        if not tmp.get(level):
            tmp[level] = {}
        tmp = tmp[level]


def print_out(subtrie, level):
    key_lst = list(subtrie.keys())
    key_lst.sort()
    for key in key_lst:
        print("--" * level + key)
        nxt = subtrie[key]
        print_out(nxt, level + 1)


print_out(trie, 0)