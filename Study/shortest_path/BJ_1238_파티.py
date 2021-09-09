# https://www.acmicpc.net/problem/1238
# 32036KB, 2596ms

import sys
from heapq import heappop, heappush

# 가는 길을 저장해두고 최댓값을 구한다?
input = sys.stdin.readline
N, M, X = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    G[u].append((v, w))


def dijkstra(start, end):
    INF = 0xfffff
    distance = [INF] * (N + 1)  # 최단거리
    P = [i for i in range(N + 1)]   # 어디서 온건지 -> 필요 없다
    visited = [0] * (N + 1)
    distance[start] = 0
    Q = [(0, start)]
    while Q:
        dis, u = heappop(Q)
        if dis > distance[u]:
            continue
        visited[u] = 1
        for v, w in G[u]:
            if not visited[v] and distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                P[v] = u
                heappush(Q, (distance[v], v))

    return distance[end]

ans = []
for i in range(1, N + 1):
    ans.append(dijkstra(i, X) + dijkstra(X, i))

print(max(ans))

'''
4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3
'''