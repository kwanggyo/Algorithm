4# 1부터 시작(시간)
# 구조물 타입에 따라 갈 수 있는 방향을 정한다.
# 도착했던 곳은 방문표시, cnt
# 1 -> 상하좌우
# 2 -> 상하
# 3 -> 좌우
# 4 -> 상우
# 5 -> 우하
# 6 -> 좌하
# 7 -> 상좌
from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    underground = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    ans = 1
    # 상 우 하 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    Q = deque()
    Q.append((R, C))
    while Q:
        r, c = Q.popleft()
        if underground[r][c] == 1:
            for k in range(4):
                nr = r + dr[k]
                nc = c + dr[k]
                if visited[nr][nc] == 0 and underground[nr][nc] != 0:
                    if 0 <= nr < N and 0 <= nc < M:
                        visited[nr][nc] = 1
                        ans += 1
                        Q.append((nr, nc))
        elif underground[r][c] == 2:
            for k in range(4):
                if k == 0 or k == 2:
                    nr = r + dr[k]
                    nc = c + dr[k]
                    if visited[nr][nc] == 0 and underground[nr][nc] != 0:
                        if 0 <= nr < N and 0 <= nc < M:
                            visited[nr][nc] = 1
                            ans += 1
                            Q.append((nr, nc))
        elif underground[r][c] == 3:
            for k in range(4):
                if k == 1 or k == 3:
                    nr = r + dr[k]
                    nc = c + dr[k]
                    if visited[nr][nc] == 0 and underground[nr][nc] != 0:
                        if 0 <= nr < N and 0 <= nc < M:
                            visited[nr][nc] = 1
                            ans += 1
                            Q.append((nr, nc))
        elif underground[r][c] == 4:
            for k in range(4):
                if k == 0 or k == 1:
                    nr = r + dr[k]
                    nc = c + dr[k]
                    if visited[nr][nc] == 0 and underground[nr][nc] != 0:
                        if 0 <= nr < N and 0 <= nc < M:
                            visited[nr][nc] = 1
                            ans += 1
                            Q.append((nr, nc))
        elif underground[r][c] == 5:
            for k in range(4):
                if k == 1 or k == 2:
                    nr = r + dr[k]
                    nc = c + dr[k]
                    if visited[nr][nc] == 0 and underground[nr][nc] != 0:
                        if 0 <= nr < N and 0 <= nc < M:
                            visited[nr][nc] = 1
                            ans += 1
                            Q.append((nr, nc))
        elif underground[r][c] == 6:
            for k in range(4):
                if k == 2 or k == 3:
                    nr = r + dr[k]
                    nc = c + dr[k]
                    if visited[nr][nc] == 0 and underground[nr][nc] != 0:
                        if 0 <= nr < N and 0 <= nc < M:
                            visited[nr][nc] = 1
                            ans += 1
                            Q.append((nr, nc))
        elif underground[r][c] == 7:
            for k in range(4):
                if k == 0 or k == 3:
                    nr = r + dr[k]
                    nc = c + dr[k]
                    if visited[nr][nc] == 0 and underground[nr][nc] != 0:
                        if 0 <= nr < N and 0 <= nc < M:
                            visited[nr][nc] = 1
                            ans += 1
                            Q.append((nr, nc))
    print(ans)


