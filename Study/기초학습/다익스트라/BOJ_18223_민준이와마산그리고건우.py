# https://www.acmicpc.net/problem/18223
# Dijkstra
# 36004KB, 116ms

from heapq import heappush, heappop
import sys

input = sys.stdin.readline

V, E, P = map(int, input().split())
route = [[] for _ in range(V + 1)]
INF = int(1e9)
for _ in range(E):
    a, b, c = map(int, input().split())
    route[a].append([c, b])
    route[b].append([c, a])


def dijkstra(start):
    HQ = []
    heappush(HQ, [0, start])
    dist = [INF] * (V + 1)

    while HQ:
        now_dist, now_node = heappop(HQ)

        if dist[now_node] < now_dist:
            continue

        for next_dist, next_node in route[now_node]:
            if now_dist + next_dist < dist[next_node]:
                dist[next_node] = now_dist + next_dist
                heappush(HQ, [dist[next_node], next_node])

    return dist

M_distance = dijkstra(1)    # 민준이가 있는 곳에서 이동
G_distance = dijkstra(P)    # 건우가 있는 곳에서 이동

# 건우가 1인 경우 예외 처리 !(99%에서 틀렸습니다)
if P == 1:
    print("SAVE HIM")
else:
    if M_distance[V] < M_distance[P] + G_distance[V]:
        print("GOOD BYE")
    else:
        print("SAVE HIM")