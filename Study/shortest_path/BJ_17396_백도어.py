# https://www.acmicpc.net/problem/17396
# 118372KB, 1228ms
# visited 사용여부 : https://www.acmicpc.net/board/view/9350
# 다잌?
# 음수 가중치 : 벨만포드
# 모든 정점 : 플로이드 와샬

import sys
from heapq import heappop, heappush

def dijkstra():
    Q = [(0, 0)]    # 현재까지의 최단 거리, 출발 노드
    D[0] = 0

    while Q:
        d, u = heappop(Q)
        if d > D[u]: continue

        for v, w in G[u]:
            if check[v] == 0 and D[v] > D[u] + w:
                D[v] = D[u] + w
                heappush(Q, (D[v], v))

input = sys.stdin.readline
N, M = map(int, input().split())
check = list(map(int, input().split()))
check[-1] = 0   # 이부분 필요!
INF = sys.maxsize   # 최댓값 사이즈 키워야함 0xffffff -> 안됨
D = [INF] * N
G = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))

dijkstra()
print(D[N-1] if D[N-1] != INF else -1)