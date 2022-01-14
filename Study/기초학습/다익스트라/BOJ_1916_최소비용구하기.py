# https://www.acmicpc.net/problem/1916
# DIJKSTRA
# 59160KB, 384ms

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def dijkstra(start):
    HQ = []
    heappush(HQ, [0, start])
    dist[start] = 0
    while HQ:
        now_cost, now_node = heappop(HQ)

        if dist[now_node] < now_cost:
            continue

        for to_node, cost in city[now_node]:
            new_cost = now_cost + cost
            if dist[to_node] > new_cost:
                dist[to_node] = new_cost
                heappush(HQ, [new_cost, to_node])


N = int(input())
M = int(input())
INF = 0xffffffff    # 크기 생각! 1000*100000 이상
city = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    city[a].append([b, c])
start, end = map(int, input().split())
dist = [INF] * (N + 1)

dijkstra(start)
print(dist[end])