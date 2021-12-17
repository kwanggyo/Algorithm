# https://www.acmicpc.net/problem/21736
# DFS
# 379300KB, 1020ms

import sys
sys.setrecursionlimit(1000000)  # 런타임에러 방지
input = sys.stdin.readline


def dfs(r, c):
    global ans
    check[r][c] = 1
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if nr < 0 or nr >= N or nc < 0 or nc >= M or check[nr][nc] == 1: continue
        if campus[nr][nc] == 'O' and check[nr][nc] == 0:
            dfs(nr, nc)
        if campus[nr][nc] == 'P' and check[nr][nc] == 0:
            ans += 1
            dfs(nr, nc)


N, M = map(int, input().split())
campus = [list(input())[:M] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            sx, sy = i, j
ans = 0
check = [[0] * M for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
dfs(sx, sy)
print('TT' if ans == 0 else ans)
