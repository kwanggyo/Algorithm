# https://www.acmicpc.net/problem/1753
# 66716KB, 828ms
# 밑에는 시간초과


import sys
from heapq import heappop, heappush

def dijstra(s):
    D = [0xfffff] * (V + 1)
    visit = [False] * (V + 1)
    D[s] = 0
    Q = [[0, s]]

    while Q:
        d, u = heappop(Q)
        if d > D[u]: continue

        visit[u] = True
        for v, w in G[u]:
            if not visit[v] and D[v] > D[u] + w:
                D[v] = D[u] + w
                heappush(Q, [D[v], v])
    return D


input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input())
G = [[] for _ in range(V + 1)]
for i in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))

ans = dijstra(start)

for i in range(1, V+1):
    if ans[i] == 0xfffff:
        print('INF')
    else:
        print(ans[i])


# import sys

# def dijstra(s):
#     D = [0xfffff] * (V + 1)
#     visit = [False] * (V + 1)
#     D[s] = 0

#     cnt = V
#     while cnt:    # 정점의 수 만큼 반복 
#         u, MIN = 0, 0xfffff
#         for i in range(1, V + 1):
#             if not visit[i] and D[i] < MIN:
#                 u, MIN = i, D[i]
#         visit[u] = True

#         for v, w in G[u]:
#             if not visit[v] and D[v] > D[u] + w:
#                 D[v] = D[u] + w
#         cnt -= 1
#     return D


# input = sys.stdin.readline
# V, E = map(int, input().split())    # 정점, 간선
# start = int(input())
# G = [[] for _ in range(V + 1)]
# for i in range(E):
#     u, v, w = map(int, input().split())
#     G[u].append((v, w))

# ans = dijstra(start)

# for i in range(1, V+1):
#     if ans[i] == 0xfffff:
#         print('INF')
#     else:
#         print(ans[i])