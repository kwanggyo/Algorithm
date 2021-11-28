# https://www.acmicpc.net/problem/2636
# 32116KB 136ms

from collections import deque
import sys

input = sys.stdin.readline


def bfs():
    check = [[0] * M for _ in range(N)]
    Q = deque()
    Q.append((0, 0))
    check[0][0] = 1
    cnt = 0
    while Q:
        r, c = Q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and check[nr][nc] == 0:
                if cheese[nr][nc] == 0:
                    check[nr][nc] = 1
                    Q.append((nr, nc))
                else:
                    check[nr][nc] = 1
                    cheese[nr][nc] = 0
                    cnt += 1
    return cnt


N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
result = []

while True:
    count = bfs()
    if count == 0:
        break
    result.append(count)

print(len(result))
print(result[-1])