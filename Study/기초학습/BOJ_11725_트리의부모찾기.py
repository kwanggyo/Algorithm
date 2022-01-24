# https://www.acmicpc.net/problem/11725
# BFS
# 49644KB, 460ms

from collections import deque
import sys
input = sys.stdin.readline

def BFS():
    Q = deque()
    Q.append(1)
    while Q:
        node = Q.popleft()
        for i in graph[node]:
            if parent[i] == 0:
                parent[i] = node
                Q.append(i)

    return parent


N = int(input())
graph = [[] for _ in range(N + 1)]
parent = [0 for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

BFS()

for i in parent[2:]:
    print(i)