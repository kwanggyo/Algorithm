# https://www.acmicpc.net/problem/1956
# Floyd-Warshall
# pypy3 127068KB, 2796ms

import sys
input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
dist = [[INF] * V for _ in range(V)]

for _ in range(E):
    a, b, ab_dist = map(int, input().split())
    dist[a-1][b-1] = ab_dist

for k in range(V):
    for i in range(V):
        for j in range(V):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

ans = INF
for i in range(V):
    ans = min(ans, dist[i][i])

print(ans if ans != INF else -1)
