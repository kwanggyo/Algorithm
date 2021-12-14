# https://www.acmicpc.net/problem/17086
# BFS
# PyPy3 131688KB, 548ms

import sys
from collections import deque

input = sys.stdin.readline

def bfs(y, x, cnt):
    res = 0
    Q = deque()
    Q.append((y, x, cnt))
    while Q:
        r, c, cnt = Q.popleft()
        res = cnt
        for k in range(8):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr >= N or nr < 0 or nc >= M or nc < 0: continue
            if box[nr][nc] == 1:
                return res
            if check[nr][nc] == 0 and box[nr][nc] == 0:
                check[nr][nc] = 1
                Q.append((nr, nc, cnt + 1))
    return res


N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
# 상 / 우 \ 하 / 좌 \
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

ans = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 1: continue
        check = [[0] * M for _ in range(N)]
        check[i][j] = 1
        tmp = bfs(i, j, 0)
        if ans < tmp:
            ans = tmp
print(ans + 1)
