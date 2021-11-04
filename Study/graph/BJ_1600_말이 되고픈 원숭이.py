# https://www.acmicpc.net/problem/1600
# bfs 재귀로 두가지로 나눠서 가게한다.

# 안되는 코드임.. 다시 풀어보기!!
# https://www.acmicpc.net/problem/2206 벽 부수기 풀어보기

from collections import deque

K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
visited = [[0] * W for _ in range(H)]
ans = []
# 상우하좌
dr = [-1, 0, 1, 0, -2, -1, 1, 2, 2, 1, -1, -2]
dc = [0, 1, 0, -1, 1, 2, 2, 1, -1, -2, -2, -1]

# dr1 = [-1, 0, 1, 0]
# dc1 = [0, 1, 0, -1]
# # 대각선 상우하좌
# dlr = [-2, -1, 1, 2, 2, 1, -1, -2]
# dlc = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(r, c, jump, cnt):
    if r == H-1 and c == W-1:
        ans.append(cnt)

    for k in range(12):
        nr = r + dr[k]
        nc = c + dc[k]
        if nr < 0 or nr >= H or nc < 0 or nc >= W:
            continue
        if visited[nr][nc] == 1 or arr[nr][nc] == 1:
            continue
        visited[nr][nc] = 1
        if k < 4:
            bfs(nr, nc, jump, cnt + 1)
        else:
            if jump > 1:
                bfs(nr, nc, jump - 1, cnt + 1)
        visited[nr][nc] = 0


# def bfs2():
#     Q = deque()
#     Q.append((0, 0, K, 0))
#     while Q:
#         r, c, jump, cnt = Q.popleft()
#         if r == H - 1 and c == W - 1:
#             return cnt
#         for k in range(4):
#             nr = r + dr1[k]
#             nc = c + dc1[k]
#             if nr < 0 or nr >= H or nc < 0 or nc >= W:
#                 continue
#             if visited[nr][nc] == 1 or arr[nr][nc] == 1:
#                 continue
#             visited[nr][nc] = 1
#             Q.append((nr, nc, jump, cnt + 1))
#         if jump > 1:
#             for k in range(8):
#                 nlr = r + dlr[k]
#                 nlc = c + dlc[k]
#                 if nlr < 0 or nlr >= H or nlc < 0 or nlc >= W:
#                     continue
#                 if visited[nlr][nlc] == 1 or arr[nlr][nlc] == 1:
#                     continue
#                 visited[nlr][nlc] = 1
#                 Q.append((nlr, nlc, jump-1, cnt + 1))
#         return -1

visited[0][0] = 1
# print(bfs2())
print(ans)
