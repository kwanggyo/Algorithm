# 대소문자가 들어가 있는 52x52 행렬을 만든다.
# 0 ~ 25 번 까지는 + 65, 26 ~ 51 까지는 + 71을 해서 알파벳을 구한다.
# 29452KB, 508ms

N = int(input())
INF = 0xffffff
alphabet = [[INF] * 52 for _ in range(52)]

for _ in range(N):
    string = input()
    if ord(string[0]) < 91:
        if ord(string[5]) < 91:
            alphabet[ord(string[0])-65][ord(string[5])-65] = 1
        else:
            alphabet[ord(string[0])-65][ord(string[5])-71] = 1
    else:
        if ord(string[5]) < 91:
            alphabet[ord(string[0])-71][ord(string[5])-65] = 1
        else:
            alphabet[ord(string[0])-71][ord(string[5])-71] = 1

for k in range(52):
    for i in range(52):
        for j in range(52):
            if alphabet[i][k] + alphabet[k][j] < INF:
                alphabet[i][j] = 1

cnt = 0
ans_li = []
for i in range(52):
    for j in range(52):
        if i != j and alphabet[i][j] == 1:
            if i < 26:
                if j < 26:
                    ans = chr(i + 65) + " => " + chr(j + 65)
                else:
                    ans = chr(i + 65) + " => " + chr(j + 71)
            else:
                if j < 26:
                    ans = chr(i + 71) + " => " + chr(j + 65)
                else:
                    ans = chr(i + 71) + " => " + chr(j + 71)
            ans_li.append(ans)

print(len(ans_li))
for val in ans_li:
    print(val)
