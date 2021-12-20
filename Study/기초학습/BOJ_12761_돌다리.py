# https://www.acmicpc.net/problem/12761
# BFS
# 35500KB, 272ms
# 갈 수 있는 방법 : +1, -1, +A, -A, +B, -B, Ax, Bx

from collections import deque
import sys
input = sys.stdin.readline


def bfs(pos, cnt):
    global ans
    Q = deque()
    Q.append((pos, cnt))
    check[pos] = 1
    while Q:
        r, count = Q.popleft()
        if r == M:
            ans = count
            return
        for k in range(6):
            nr = r + dr[k]
            if nr < 0 or nr > 100000 or check[nr] == 1: continue
            check[nr] = 1
            Q.append((nr, count + 1))
        for l in range(4, 6):
            nr = r*dr[l]
            if nr < 0 or nr > 100000 or check[nr] == 1: continue
            check[nr] = 1
            Q.append((nr, count + 1))


A, B, N, M = map(int, input().split())
ans = 100000    # 0개수 확인!!
dr = [1, -1, -A, -B, A, B]
check = [0] * 100001
bfs(N, 0)
print(ans)