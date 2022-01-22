# https://www.acmicpc.net/problem/1504
# DIJKSTRA
# 1 -> v1 -> v2 -> N, 1 -> v2 -> v1 -> N 으로 이동하는 최단거리를 비교
# 67688KB, 644ms

from heapq import heappush ,heappop
import sys
input = sys.stdin.readline

def dijkstra(start):
    dist = [INF] * (N + 1)
    HQ = []
    heappush(HQ, [0, start])
    dist[start] = 0
    while HQ:
        now_dist, now_node = heappop(HQ)

        if dist[now_node] < now_dist:
            continue

        for next_dist, next_node in G[now_node]:
            if now_dist + next_dist < dist[next_node]:
                dist[next_node] = now_dist + next_dist
                heappush(HQ, [dist[next_node], next_node])
    return dist

N, E = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, dist = map(int, input().split())
    G[a].append([dist, b])
    G[b].append([dist, a])
v1, v2 = map(int, input().split())
INF = int(1e9)

# 1에서 최단 거리, v1에서 최단거리, v2에서 최단거리를 각각 계산해놓고 더한다.
first_dist = dijkstra(1)
v1_dist = dijkstra(v1)
v2_dist = dijkstra(v2)
v1_path = first_dist[v1] + v1_dist[v2] + v2_dist[N]
v2_path = first_dist[v2] + v2_dist[v1] + v1_dist[N]
ans = min(v1_path, v2_path)

print(ans if ans < INF else -1)




