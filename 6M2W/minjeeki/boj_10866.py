# 실버 4. 덱
# pr-agent 테스트용 문제 풀이 코드 업로드 (스택 두개로 덱 구현)
import sys
input = sys.stdin.readline

front_stack = []
len_front_stack = 0
idx_last_front_stack = 0
back_stack = []
len_back_stack = 0
idx_first_back_stack = 0

N = int(input())
for _ in range(N):
    line = input().split()
    if line[0] == "push_front":
        push_num = int(line[1])
        if len_back_stack == 0 and len_front_stack == 0:
            back_stack.append(push_num)
            len_back_stack += 1
        else:
            front_stack.append(push_num)
            len_front_stack += 1
    elif line[0] == "push_back":
        push_num = int(line[1])
        back_stack.append(push_num)
        len_back_stack += 1
    elif line[0] == "pop_front" or line[0] == "front":
        if len_front_stack == 0 and len_back_stack == 0:
            print(-1)
        elif len_front_stack == 0:
            print(back_stack[idx_first_back_stack])
            if line[0] == "pop_front":
                back_stack[idx_first_back_stack] = -1
                idx_first_back_stack += 1
                len_back_stack -= 1
        else:
            print(front_stack[-1])
            if line[0] == "pop_front":
                front_stack.pop()
                len_front_stack -= 1
    elif line[0] == "pop_back" or line[0] == "back":
        if len_back_stack == 0 and len_front_stack == 0:
            print(-1)
        elif len_back_stack == 0:
            print(front_stack[idx_last_front_stack])
            if line[0] == "pop_back":
                front_stack[idx_last_front_stack] = -1
                idx_last_front_stack += 1
                len_front_stack -= 1
        else:
            print(back_stack[-1])
            if line[0] == "pop_back":
                back_stack.pop()
                len_back_stack -= 1
    elif line[0] == "size":
        print(len_front_stack + len_back_stack)
    elif line[0] == "empty":
        if len_front_stack == 0 and len_back_stack == 0:
            print(1)
        else:
            print(0)
