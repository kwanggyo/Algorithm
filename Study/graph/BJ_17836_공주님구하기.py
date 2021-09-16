# https://www.acmicpc.net/problem/17836
# 검의 위치를 (x, y)라 하면 검까지 걸린 시간에서 abs(N-x) + abs(M-y) 시간을 더해준다.
# 31932KB, 116ms

import sys
from collections import deque

input = sys.stdin.readline
N, M, T = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
Q = deque()
Q.append((0, 0, 0))
visited[0][0] = 1
ans = 10001

while Q:
    r, c, time = Q.popleft()
    if time > ans: break
    if r == N-1 and c == M-1:
        ans = time
        break
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
            if maze[nr][nc] == 1:
                continue
            elif maze[nr][nc] == 2:
                visited[nr][nc] = 1
                ans = time + 1 + abs(N-1-nr) + abs(M-1-nc)
            else:
                visited[nr][nc] = 1
                Q.append((nr, nc, time + 1))

if ans > T:
    print('Fail')
else:
    print(ans)


# 반례
'''
6 6 16
0 0 0 0 1 1
0 0 0 0 0 0
1 1 1 0 1 0
2 0 0 0 0 0
1 1 1 1 0 1
0 0 0 0 0 0
'''