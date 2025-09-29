from collections import deque

L, C = map(int, input().split())
letters = input().split()
letters.sort()
vowels, consonants = [], []
for letter in letters:
    if letter in ['a', 'e', 'i', 'o', 'u']:
        vowels.append(letter)
    else:
        vowels.append(consonants)

def condition(code):
    nv, nc = 0, 0
    for letter in code:
        if letter in 'aeiou':
            nv += 1
        else:
            nc += 1
    if nv >= 1 and nc >= 2:
        return True
    return False

queue = deque(letters[:])
while queue:
    code = queue.popleft()
    if len(code) == L and condition(code):
        print(code)
    else:
        for i in range(letters.index(code[-1]) + 1, C):
            queue.append(code + letters[i])
