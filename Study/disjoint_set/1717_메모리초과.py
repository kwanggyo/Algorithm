# N, M의 범위를 봤을 때 for문 한개를 써야할 듯?
# dict에 M개를 만든다.
# 0이 나오면 추가, 1이 나오면 출력

N, M = map(int, input().split())
number = dict()
for i in range(N+1):
    number[i] = set()
    number[i].add(i)

for j in range(M):
    a, b, c = map(int, input().split())
    if a == 0:
        number[b].add(c)
        number[c].add(b)
    else:
        if c in number[b] or b in number[c]:
            print('YES')
        else:
            print('NO')