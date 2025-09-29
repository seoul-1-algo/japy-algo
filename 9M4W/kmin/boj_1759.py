import sys
input = sys.stdin.readline
L, C = map(int, input().split())
letters = list(input().split())
letters.sort()
vowels = ["a", "e", "i", "o", "u"]
answer = []

def check(arr):
    vcount, ccount = 0, 0   # vowel, consonant 갯수
    for i in arr:
        if i in vowels:
            vcount += 1
        else:
            ccount += 1
    
    if vcount >= 1 and ccount >= 2: # 최소 한개의 모음, 2개의 자음
        return True
    else:
        return False

def back(arr):
    if len(arr) == L:   
        if check(arr):
            print("".join(arr))
            return
    
    for i in range(len(arr), C):    # 고른 문자 갯수(len(arr))을 기준으로, 사전적으로 큰 알파벳 선택
        if arr[-1] < letters[i]:    # 문자열의 마지막보다 사전적으로 큰 알파벳인지 확ㅇ니
            arr.append(letters[i])
            back(arr)   # 재귀
            arr.pop()   # 백트래킹

for i in range(C - L + 1):
    a = [letters[i]]
    back(a)