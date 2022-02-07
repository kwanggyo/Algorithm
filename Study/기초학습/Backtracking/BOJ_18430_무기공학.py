# https://www.acmicpc.net/problem/18430
# Backtracking
# 30864KB, 1576ms
# 다시 풀어보기 !

# 부메랑을 만들 수 있는지 확인
# 부메랑을 안만들고 넘어가거나 만들고 점수를 합산하여 진행

import sys
input = sys.stdin.readline

def dfs(r, c, total):
    global ans
    # 오른쪽 끝에 도착하면 다음 줄로 내려가서 계산
    if c == M:
        c = 0
        r += 1
    # 제일 아랫줄에 도착했다면 그만
    if r == N:
        if ans < total:
            ans = total
        return
    # 계산 안하고 넘어가는 부분
    dfs(r, c + 1, total)
    for boo in  boomerang:
        # 상하 부분(1), 좌우 부분(2)
        dr1 = r + boo[0][0]
        dc1 = c + boo[0][1]
        dr2 = r + boo[1][0]
        dc2 = c + boo[1][1]
        # 바운드리, 방문 체크
        if 0 <= dr1 < N and 0 <= dr2 < N and 0 <= dc1 < M and 0 <= dc2 < M:
            if visited[r][c] != 1 and visited[dr1][dc1] != 1 and visited[dr2][dc2] != 1:
                visited[r][c], visited[dr1][dc1], visited[dr2][dc2] = 1, 1, 1
                dfs(r, c + 1, total + material[r][c] * 2 + material[dr1][dc1] + material[dr2][dc2])
                visited[r][c], visited[dr1][dc1], visited[dr2][dc2] = 0, 0, 0


N, M = map(int, input().split())
material = [list(map(int, input().split())) for _ in range(N)]
# 기준점으로부터 하우, 하좌, 상우, 상좌
boomerang = [[(1, 0), (0, 1)], [(1, 0), (0, -1)], [(-1, 0), (0, 1)], [(-1, 0), (0, -1)]]
visited = [[0] * M for _ in range(N)]
ans = 0
dfs(0, 0, 0)
print(ans)