# https://www.acmicpc.net/problem/18430
# 4가지 경우의 수를 체크한다.(리스트로 만들어서)
# 방문체크를 한다.
# 29200KB, 1604ms

def dfs(r, c, total):
    global ans
    if c == M:
        c = 0
        r += 1
    if r == N:
        if ans < total:
            ans = total
        return
    dfs(r, c + 1, total)
    for k in dir:
        dr1 = r + k[0][0]
        dc1 = c + k[0][1]
        dr2 = r + k[1][0]
        dc2 = c + k[1][1]
        if 0 <= dr1 < N and 0 <= dc1 < M and 0 <= dr2 < N and 0 <= dc2 < M:
            if check[r][c] != 1 and check[dr1][dc1] != 1 and check[dr2][dc2] != 1:
                check[r][c], check[dr1][dc1], check[dr2][dc2] = 1, 1, 1
                dfs(r, c + 1, total + 2 * arr[r][c] + arr[dr1][dc1] + arr[dr2][dc2])
                check[r][c], check[dr1][dc1], check[dr2][dc2] = 0, 0, 0


N, M = map(int, input().split())    # 세로, 가로
arr = [list(map(int, input().split())) for _ in range(N)]
# 우하 / 하좌 / 좌상 / 상우
dir = [[(0, 1), (1, 0)], [(1, 0), (0, -1)], [(-1, 0), (0, -1)], [(-1, 0), (0, 1)]]
check = [[0] * M for _ in range(N)]
ans = 0
dfs(0, 0, 0)
print(ans)