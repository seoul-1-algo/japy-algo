l,c = map(int,input().split())
letters = input().split()
letters.sort()

vowels = ['a','e','i','o','u']

def pwcheck(pw):
    moum, jaum = 0,0
    for i in pw:
        if i in vowels:
            moum+=1
        else:
            jaum+=1
    
    if moum >= 1 and jaum >= 2:
        return True
    else:
        return False

# 차피 알파벳순 정렬된 문자를 pw에 넣어줄거임.
def backtrack(nowpw):
    # 만족하는 길이의 암호면 출력
    if len(nowpw) == l:
        if pwcheck(nowpw):
            print("".join(nowpw))
            return
    
    for i in range(len(nowpw), c):
        if nowpw[-1] < letters[i]:
            nowpw.append(letters[i])
            backtrack(nowpw)
            nowpw.pop()

# letter에 들어있는 글자를 골랐을 때, 남아있는 고를 수 있는 글자가 너무 적으면 안됨.
for i in range(c-l+1):
    pw = [letters[i]]
    backtrack(pw)