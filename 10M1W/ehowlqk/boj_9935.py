text = input()
bomb = input()
bomb_len = len(bomb)

while 1:
    # 새로 생긴 문자열에 폭발 문자열이 포함되는지 확인
    i = text.find(bomb)
    # 없다면 반복을 탈출한다.
    if i < 0:
        break
    # 폭발할 문자열의 시작과 끝 인덱스를 정의한다.
    start, end = i, i + bomb_len
    while 1:
        # 폭발 문자열 제외 앞뒤로 폭발 문자열의 길이만큼 봄 -> 폭발 뒤 합쳐진 문자열에서도 폭발할 수 있는지 확인
        tmp = text[start-bomb_len:start] + text[end:end+bomb_len]
        # 만약 폭발 후 또 폭발할 수 있다면
        idx = tmp.find(bomb)
        if idx > 0:
            start = start - bomb_len + idx  # start 인덱스 재조정
            end = end + idx                 # end 인덱스 재조정
        else:break
    
    text = text[:start] + text[end:]    # 폭발 후 문자열 재할당
    
print(text if text else "FRULA")
