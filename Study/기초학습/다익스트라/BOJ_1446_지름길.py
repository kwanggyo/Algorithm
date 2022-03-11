# https://www.acmicpc.net/problem/1446
# Dijkstra
# 30864KB, 80ms

import sys
input = sys.stdin.readline

N, D = map(int, input().split())
arr = [[] for _ in range(10001)]

for _ in range(N):
    s, e, dist = map(int, input().split())
    arr[s].append([dist, e])

distance = [i for i in range(D + 1)]

for i in range(D + 1):
    if i != 0:
        distance[i] = min(distance[i], distance[i -  1] + 1)
    for dist, e in arr[i]:
        if e <= D and distance[e] > dist + distance[i]:
            distance[e] = dist + distance[i]

print(distance[D])