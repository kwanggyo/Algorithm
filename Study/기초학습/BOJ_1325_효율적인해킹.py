# https://www.acmicpc.net/problem/1325
# 플로이드와샬

import sys
input = sys.stdin.readline


def dfs(v):
    global cnt
    for w in G[v]:
        if check[w] == 1: continue
        check[w] = 1
        cnt += 1
        dfs(w)


N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)

ans = 0
for i in range(1, N+1):
    check = [0] * (N + 1)
    cnt = 0
    dfs(i)
    if ans < cnt:
        ans = cnt

print(ans)



