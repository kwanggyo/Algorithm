# https://www.acmicpc.net/problem/22944
# 라이프와 우산을 변수로 우산이 있을시 라이프 감소 x
# 우산을 가지고 있는지 판단해야한다.
# 시간 초과

from collections import deque

import sys
input = sys.stdin.readline
N, H, D = map(int, input().split())
death_rain = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
flag = False
# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
Q = deque()

for i in range(N):
    for j in range(N):
        if death_rain[i][j] == 'S':
            Q.append((i, j, H, 0, 0))

ans = -1
while Q and not flag:
    r, c, life, umbrella, time = Q.popleft()
    visited[r][c] = H
    if life == 0:
        continue
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N:
            cnt = time + 1
            current_umbrella = umbrella
            current_life = life
            if death_rain[nr][nc] == 'E':
                ans = cnt
                flag = True
            elif death_rain[nr][nc] == 'U':
                current_umbrella = D

            if current_umbrella == 0:
                current_life -= 1
            else:
                current_umbrella -= 1
            
            if current_life == 0:
                continue

            if visited[nr][nc] < current_life:
                visited[nr][nc] = current_life
                Q.append((nr, nc, current_life, current_umbrella, cnt))

print(ans)
