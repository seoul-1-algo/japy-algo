str1 = input()
str2 = input()

table = [['' for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i-1] == str2[j-1]:
            table[i][j] = table[i-1][j-1] + str1[i-1]
        else:
            if len(table[i-1][j]) > len(table[i][j-1]):
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = table[i][j-1]

answer = table[-1][-1]
print(len(answer))
print(answer)