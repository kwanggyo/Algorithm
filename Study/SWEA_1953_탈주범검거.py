# 1부터 시작(시간)
# 구조물 타입에 따라 갈 수 있는 방향을 정한다.
# 도착했던 곳은 방문표시, cnt
# 1 -> 상하좌우
# 2 -> 상하
# 3 -> 좌우
# 4 -> 상우
# 5 -> 우하
# 6 -> 좌하
# 7 -> 상좌
# 서로 모양을 생각해야함 ㅡ와 ㅣ 는 연결 불가 !
# 각각 연결가능할 때 cnt를 추가하는 방식 -> 조건이 너무 많다..
def dfs(r, c, hour):
    global cnt
    if hour == L:
        return
    if underground[r][c] == 1:
        for k in range(4):          # 상 우 하 좌
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and underground[nr][nc] != 0 and visited[nr][nc] == 0:
                if k == 0:
                    if underground[nr][nc] == 1 or underground[nr][nc] == 2 or underground[nr][nc] == 5 or underground[nr][nc] == 6:
                        visited[nr][nc] = 1
                        cnt += 1
                        dfs(nr, nc, hour + 1)
                elif k == 1:
                    if underground[nr][nc] == 1 or underground[nr][nc] == 3 or underground[nr][nc] == 6 or underground[nr][nc] == 7:
                        visited[nr][nc] = 1
                        cnt += 1
                        dfs(nr, nc, hour + 1)
                elif k == 2:
                    if underground[nr][nc] == 1 or underground[nr][nc] == 2 or underground[nr][nc] == 4 or underground[nr][nc] == 7:
                        visited[nr][nc] = 1
                        cnt += 1
                        dfs(nr, nc, hour + 1)
                elif k == 3:
                    if underground[nr][nc] == 1 or underground[nr][nc] == 3 or underground[nr][nc] == 4 or underground[nr][nc] == 5:
                        visited[nr][nc] = 1
                        cnt += 1
                        dfs(nr, nc, hour + 1)
    elif underground[r][c] == 2:
        for k in range(4):
            if k == 0 or k == 2:    # 상 하
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < M and underground[nr][nc] != 0 and visited[nr][nc] == 0:
                    if k == 0:
                        if underground[nr][nc] == 1 or underground[nr][nc] == 2 or underground[nr][nc] == 5 or underground[nr][nc] == 6:
                            visited[nr][nc] = 1
                            cnt += 1
                            dfs(nr, nc, hour + 1)
                    elif k == 2:
                        if underground[nr][nc] == 1 or underground[nr][nc] == 2 or underground[nr][nc] == 4 or underground[nr][nc] == 7:
                            visited[nr][nc] = 1
                            cnt += 1
                            dfs(nr, nc, hour + 1)
    elif underground[r][c] == 3:
        for k in range(4):
            if k == 1 or k == 3:    # 좌 우
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < M and underground[nr][nc] != 0 and visited[nr][nc] == 0:
                    if k == 1:
                        if underground[nr][nc] == 1 or underground[nr][nc] == 3 or underground[nr][nc] == 6 or underground[nr][nc] == 7:
                            visited[nr][nc] = 1
                            cnt += 1
                            dfs(nr, nc, hour + 1)
                    elif k == 3:
                        if underground[nr][nc] == 1 or underground[nr][nc] == 3 or underground[nr][nc] == 4 or underground[nr][nc] == 5:
                            visited[nr][nc] = 1
                            cnt += 1
                            dfs(nr, nc, hour + 1)
    elif underground[r][c] == 4:
        for k in range(4):
            if k == 0 or k == 1:    # 상 우
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < M and underground[nr][nc] != 0 and visited[nr][nc] == 0:
                    if k == 0:
                        if underground[nr][nc] == 1 or underground[nr][nc] == 2 or underground[nr][nc] == 5 or underground[nr][nc] == 6:
                            visited[nr][nc] = 1
                            cnt += 1
                            dfs(nr, nc, hour + 1)
                    elif k == 1:
                        if underground[nr][nc] == 1 or underground[nr][nc] == 3 or underground[nr][nc] == 6 or underground[nr][nc] == 7:
                            visited[nr][nc] = 1
                            cnt += 1
                            dfs(nr, nc, hour + 1)
    elif underground[r][c] == 5:
        for k in range(4):
            if k == 1 or k == 2:    # 우 하
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < M and underground[nr][nc] != 0 and visited[nr][nc] == 0:
                    if k == 1:
                        if underground[nr][nc] == 1 or underground[nr][nc] == 3 or underground[nr][nc] == 6 or underground[nr][nc] == 7:
                            visited[nr][nc] = 1
                            cnt += 1
                            dfs(nr, nc, hour + 1)
                    elif k == 2:
                        if underground[nr][nc] == 1 or underground[nr][nc] == 2 or underground[nr][nc] == 4 or underground[nr][nc] == 7:
                            visited[nr][nc] = 1
                            cnt += 1
                            dfs(nr, nc, hour + 1)
    elif underground[r][c] == 6:
        for k in range(4):
            if k == 2 or k == 3:    # 하 좌
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < M and underground[nr][nc] != 0 and visited[nr][nc] == 0:
                    if k == 2:
                        if underground[nr][nc] == 1 or underground[nr][nc] == 2 or underground[nr][nc] == 4 or underground[nr][nc] == 7:
                            visited[nr][nc] = 1
                            cnt += 1
                            dfs(nr, nc, hour + 1)
                    elif k == 3:
                        if underground[nr][nc] == 1 or underground[nr][nc] == 3 or underground[nr][nc] == 4 or underground[nr][nc] == 5:
                            visited[nr][nc] = 1
                            cnt += 1
                            dfs(nr, nc, hour + 1)
    elif underground[r][c] == 7:
        for k in range(4):
            if k == 0 or k == 3:    # 상 좌
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < M and underground[nr][nc] != 0 and visited[nr][nc] == 0:
                    if k == 0:
                        if underground[nr][nc] == 1 or underground[nr][nc] == 2 or underground[nr][nc] == 5 or underground[nr][nc] == 6:
                            visited[nr][nc] = 1
                            cnt += 1
                            dfs(nr, nc, hour + 1)
                    elif k == 3:
                        if underground[nr][nc] == 1 or underground[nr][nc] == 3 or underground[nr][nc] == 4 or underground[nr][nc] == 5:
                            visited[nr][nc] = 1
                            cnt += 1
                            dfs(nr, nc, hour + 1)


T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    underground = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    cnt = 1
    # 상 우 하 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    visited[R][C] = 1
    dfs(R, C, 1)

    # for i in range(N):
    #     for j in range(M):
    #         if visited[i][j] == 1:
    #             ans += 1
    print('#{} {}'.format(tc, cnt))
