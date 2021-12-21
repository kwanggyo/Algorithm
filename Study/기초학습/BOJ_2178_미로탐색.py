# https://www.acmicpc.net/problem/2178
# BFS
# 32084KB, 108ms

from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    while Q:
        r, c, cnt = Q.popleft()
        if r == N-1 and c == M-1:
            return cnt
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
            if visited[nr][nc] == 1 or maze[nr][nc] =='0': continue
            visited[nr][nc] = 1
            Q.append((nr, nc, cnt + 1))


N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
Q = deque()
Q.append((0, 0, 0))
visited[0][0] = 1
print(bfs() + 1)