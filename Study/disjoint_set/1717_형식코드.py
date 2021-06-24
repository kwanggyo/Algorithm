def graph(S):
    while S:
        x,y = S.pop()
        for i in range(n):
            if li[y][i] == 1:
                if li[x][i] ==1:
                    continue
                else:
                    li[x][i] = 1
                    S.append((x,i))


n = int(input())
li = list()
s = list()
for i in range(n):
    li.append(list(map(int,input().split())))

for x in range(n):
    for y in range(n):
        if li[x][y]==1:
            s.append((x,y))

graph(s)
for i in li:
    for j in i:
        print(j,end=' ')
    print('')