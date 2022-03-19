# https://www.acmicpc.net/problem/2615
# 구현
# 30864KB, 72ms

import sys
input = sys.stdin.readline

Omok = [list(map(int, input().split())) for _ in range(19)]
# 하(↓), 우하(⬊), 우(➞), 우상(⬈)
dr = [1, 1, 0, -1]
dc = [0, 1, 1, 1]


def omok():
    for r in range(19):
        for c in range(19):
            if Omok[r][c]:
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    cnt = 1

                    if nr < 0 or nc < 0 or nr >= 19 or nc >= 19:
                        continue

                    while 0 <= nr < 19 and 0 <= nc < 19 and Omok[r][c] == Omok[nr][nc]:
                        cnt += 1

                        if cnt == 5:
                            # 육목 판정 1
                            if 0 <= nr + dr[k] < 19 and 0 <= nc + dc[k] < 19 and Omok[nr][nc] == Omok[nr + dr[k]][
                                nc + dc[k]]:
                                break
                            # 육목 판정 2
                            if 0 <= r - dr[k] < 19 and 0 <= c - dc[k] < 19 and Omok[r][c] == Omok[r - dr[k]][
                                c - dc[k]]:
                                break
                            # 육목이 아닌 오목이면 return
                            return Omok[r][c], r + 1, c + 1

                        nr += dr[k]
                        nc += dc[k]
    # 승부가 나지 않을 때
    return 0, -1, -1


color, x, y = omok()
if not color:
    print(color)
else:
    print(color)
    print(x, y)
