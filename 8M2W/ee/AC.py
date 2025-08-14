import sys
sys.stdin = open('5430.txt')

T = int(input()) # 테스트 케이스 수

for _ in range(T):
    commands = list(input()) # 명령어

    n = int(input()) # 배열에 들어있는 수의 개수
    arr = list(input().strip("[]").split(",")) # 수 배열

    is_forward = True 
    is_error = False

    answer = ''

    front = 0
    rear = n - 1

    for command in commands:
        if command == 'R': # 뒤집기
            is_forward = not is_forward # 방향 뒤집기
        else: # 버리기
            if front > rear:
                answer = "error"
                break
    
            if is_forward: # 정방향이면
                front += 1
            else:
                rear -= 1

    if not answer:
        answer = arr[front : rear + 1]
        if not is_forward:
            answer = answer[::-1]
        
        answer = "[" + ",".join(answer) + "]"
        
    print(answer)
