import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    is_not_error = True
    reverse = False
    func = input()[:-1]
    n = int(input())
    arr = input()[1:-2]
    if n != 0:
        nums = list(map(str, arr.split(',')))
    else:
        nums = []
    for letter in func:
        
        if letter == 'R' and not reverse:
            reverse = True
        elif letter == 'R':
            reverse = False
        
        if letter == 'D':
            if not nums:
                print('error')
                is_not_error = False
                break
            elif reverse:
                nums.pop()
            else:
                nums.pop(0)
    if reverse:
        nums.reverse()
    if is_not_error:
        string = "["+",".join(nums)+"]"
        print(string)