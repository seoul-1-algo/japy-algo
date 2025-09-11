def stars(depth):
    if depth == 3:
        return ['  *  ', ' * * ', '*****']  # 단위 도형의 1, 2, 3번째 줄

    fractal = stars(depth // 2)
    top, bottom = [], []
    for i in range(depth // 2):
        top.append(' ' * (depth // 2) + fractal[i] + ' ' * (depth // 2))    # 삼각형 형태의 위쪽 도형
        bottom.append(fractal[i] + ' ' + fractal[i])                        # 삼각형 형태의 아래쪽 도형
    return top + bottom


n = int(input())
for row in stars(n):
    print(row)  # 각 줄 출력
