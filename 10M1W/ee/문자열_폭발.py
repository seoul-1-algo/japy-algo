import sys
sys.stdin = open('9935.txt')

string = input()
bomb = list(input())

B = len(bomb)
ans = []

for s in string:
    ans.append(s)
    if ans[-B:] == bomb:
        del ans[-B:]

print(''.join(ans) if ans else "FRULA")


# while True:
#     pres = ''.join(prev.split(bomb))
    
#     if pres == prev:
#         break

#     prev = pres

# print(pres if pres else "FRULA")