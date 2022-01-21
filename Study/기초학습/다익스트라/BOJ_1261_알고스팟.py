# https://www.notion.so/01-17-01-23-b265e4483d834ee79835782037b46319
# DIJKSTRA
# 32932KB, 100ms
# 2665 미로만들기와 같은 문제

from heapq import heappush, heappop

def dijkstra():
    HQ = []
    heappush(HQ, [0, 0, 0])
    visited[0][0] = 1
    while HQ:
        wall_cnt, r, c = heappop(HQ)
        if r == M - 1 and c == N - 1:
            return wall_cnt
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < M and 0 <= nc < N and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                if maze[nr][nc] == '0':
                    heappush(HQ, [wall_cnt, nr, nc])
                else:
                    heappush(HQ, [wall_cnt + 1, nr, nc])


N, M = map(int, input().split())
maze = [list(input()) for _ in range(M)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
visited = [[0] * N for _ in range(M)]
print(dijkstra())