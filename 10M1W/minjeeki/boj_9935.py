# 골드 4 문자열 폭발

word = input()
explosion_word = list(input())

len_word = len(word)
len_explosion_word = len(explosion_word)
all_explosion = list("FRULA")

stack = []
last = explosion_word[-1]

for ch in word:
    stack.append(ch)
    # 마지막 문자와 동일한 값이 들어오면, 스택 끝을 살펴봄
    if ch == last and len(stack) >= len_explosion_word:
        # 스택 끝의 문자들 조합이 동일하면 통째로 삭제
        tail_stack = stack[-len_explosion_word:]
        if tail_stack == explosion_word:
            del stack[-len_explosion_word:]

print(*stack if stack else all_explosion, sep='')