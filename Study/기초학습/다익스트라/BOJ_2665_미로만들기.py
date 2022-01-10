# https://www.acmicpc.net/problem/2665
# BFS
# 32448KB, 212ms

from collections import deque


def BFS():
    Q = deque()
    Q.append((0, 0, 0))
    visited[0][0][0] = 1
    while Q:
        r, c, cnt = Q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
            # 방문 안한 경우
            if visited[nr][nc][0] == 0:
                visited[nr][nc][0] = 1
                # 벽이 아닌 경우
                if room[nr][nc] == '1':
                    visited[nr][nc][1] = cnt
                    Q.append((nr, nc, cnt))
                # 벽인 경우
                else:
                    visited[nr][nc][1] = cnt + 1
                    Q.append((nr, nc, cnt + 1))
            # 방문 한 경우에
            elif visited[nr][nc][0] == 1:
                # 벽이 아닌 경우
                if room[nr][nc] == '1':
                    # 부순 벽의 개수가 더 작으면
                    if visited[nr][nc][1] > cnt:
                        visited[nr][nc][1] = cnt
                        Q.append((nr, nc, cnt))
                # 벽인 경우
                else:
                    # 부순 벽의 개수가 더 작으면
                    if visited[nr][nc][1] > cnt + 1:
                        visited[nr][nc][1] = cnt + 1
                        Q.append((nr, nc, cnt + 1))


N = int(input())
room = [list(input()) for _ in range(N)]
visited = [[[0, 0] for _ in range(N)] for _ in range(N)]  # idx 0 : 방문체크, 1 : 벽의 개수
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

BFS()
print(visited[N-1][N-1][1])