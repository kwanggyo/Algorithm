# https://www.acmicpc.net/problem/14938
# DIJKSTRA
# 32932KB, 76ms

from heapq import heappush, heappop
import sys
imput = sys.stdin.readline

def dijkstra(start):
    HQ = []
    HQ.append((0, start))
    distance = [INF] * (N + 1)
    distance[start] = 0

    while HQ:
        now_dis, now_node = heappop(HQ)
        for next_dis, next_node in G[now_node]:
            if now_dis + next_dis < distance[next_node]:
                distance[next_node] = now_dis + next_dis
                heappush(HQ, (now_dis + next_dis, next_node))

    return distance


N, M, R = map(int, input().split())
items = [0] + list(map(int, input().split()))
G = [[] for _ in range(N + 1)]
for _ in range(R):
    a, b, dist = map(int, input().split())
    G[a].append((dist, b))
    G[b].append((dist, a))
INF = 0xffffff
max_val = 0

for i in range(1, N + 1):
    temp_sum = 0
    result = dijkstra(i)
    for j in range(1, N + 1):
        if result[j] <= M:
            temp_sum += items[j]
    max_val = max(max_val, temp_sum)

print(max_val)