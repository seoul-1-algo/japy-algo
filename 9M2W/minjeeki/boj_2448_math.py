n = int(input())
S = ["  *  ",
    " * * ",
    "*****"]
h = 3
# while문을 돌면서 S에 공백과 별을 추가하며 갱신함
# top은 좌우 공백 추가된 위쪽 삼각형, bottom은 아래쪽 삼각형 * 2
while h < n:
    pad = " " * h
    top = [pad + row + pad for row in S]
    bottom = [row + " " + row for row in S]
    S = top + bottom
    h *= 2
print("\n".join(S))
