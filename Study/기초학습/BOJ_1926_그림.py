# https://www.acmicpc.net/problem/1926
# BFS
# 37104KB, 652ms

from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    global cnt
    while Q:
        r, c = Q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
            if picture[nr][nc] == 1 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                cnt += 1
                Q.append((nr, nc))
    ans.append(cnt)


N, M = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = []
Q = deque()
for i in range(N):
    for j in range(M):
        if picture[i][j] == 1 and visited[i][j] == 0:
           visited[i][j] = 1
           Q.append((i, j))
           cnt = 1
           bfs()

if len(ans):
    print(len(ans))
    print(sorted(ans)[-1])
else:   # 없는 경우 처리하기!! -> 없으면 런타임에러 발생
    print(0)
    print(0)