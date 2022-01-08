# https://www.acmicpc.net/problem/18352
# BFS, Dijstra
# BFS : 98208KB, 1588ms

from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, cnt):
    Q = deque()
    Q.append((start, cnt))
    visited[start] = 1
    while Q:
        node, dist = Q.popleft()
        if dist == K:
            ans.append(node)
            continue
        for w in city[node]:
            if visited[w] == 1: continue
            Q.append((w, dist + 1))
            visited[w] = 1  # 여기서 방문 체크를 해줘야 최단거리 체크가 가능하다.


N, M, K, X = map(int, input().split())  # 도시의 개수, 도로의 개수, 거리정보, 출발 정보
INF = 0xffffff
city = [[] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    city[A].append(B)
visited = [0] * (N + 1)
ans = []

bfs(X, 0)
ans.sort()

if len(ans):
    for val in ans:
        print(val)
else:
    print(-1)
