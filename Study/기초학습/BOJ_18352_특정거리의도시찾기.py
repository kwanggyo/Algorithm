# https://www.acmicpc.net/problem/18352
# BFS
# 98996KB 1704ms

from collections import deque
import sys
input = sys.stdin.readline

def bfs(s, cnt):
    Q = deque()
    Q.append((s, cnt))
    check = [0] * (N + 1)
    check[s] = 1
    while Q:
        v, dist = Q.popleft()
        if dist == K:
            ans.append(v)
            continue
        for w in G[v]:
            if check[w]: continue
            Q.append((w, dist + 1))
            check[w] = 1


N, M, K, X = map(int, input().split())
G = [[] for _ in range(N + 1)]
ans = []
for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)

bfs(X, 0)
ans = sorted(ans)
if len(ans) == 0:
    print(-1)
else:
    for val in ans:
        print(val)