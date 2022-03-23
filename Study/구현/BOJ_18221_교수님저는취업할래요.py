# https://www.acmicpc.net/problem/18221
# 구현

N = int(input())
desk = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if desk[i][j] == 5:
            pr, pc = i, j
        elif desk[i][j] == 2:
            sr, sc = i, j


if ((abs(pr - sr) + 1) ** 2 + (abs(pc - sc) + 1) ** 2) ** 0.5 < 5:
    print(0)
else:
    cnt = 0
    if pr < sr:
        for i in range(pr, sr):
            for j in range(pc, sc):
                if desk[i][j] == 1:
                    cnt += 1
    elif pr == sr:
        for i in range(pc, sc):
            if desk[pr][i] == 1:
                cnt += 1
    else:
        for i in range(sr, pr):
            for j in range(sc, pc):
                if desk[i][j] == 1:
                    cnt += 1
    if cnt >= 3:
        print(1)
    else:
        print(0)
