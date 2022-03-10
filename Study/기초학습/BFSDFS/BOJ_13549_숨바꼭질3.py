# https://www.acmicpc.net/problem/13549
# BFS
# 34764KB, 164ms

from collections import deque


N, K = map(int, input().split())
Q = deque()
visited = [-1] * 100001
Q.append(N)
visited[N] = 0

while Q:
    x = Q.popleft()
    if x == K:
        print(visited[x])
        break
    # 순간이동 x * 2
    if 0 <= x * 2 <= 100001 and visited[x * 2] == -1:
        visited[x * 2] = visited[x]
        # appendleft를 통해 큐의 앞에 넣어 우선순위를 가지게 한다.
        Q.appendleft(x * 2)
    # x - 1
    if 0 <= x - 1 < 100001 and visited[x - 1] == -1:
        visited[x - 1] = visited[x] + 1
        Q.append(x - 1)
    # x + 1
    if 0 <= x + 1 < 100001 and visited[x + 1] == -1:
        visited[x + 1] = visited[x] + 1
        Q.append(x + 1)