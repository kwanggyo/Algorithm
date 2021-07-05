# 0, 2 ... 등 짝수 행은 우하상좌 + (-1, 1), (1, 1)
# 1, 3 ... 등 홀수 행은 우하상좌 + (-1, -1), (1, -1)
# 내부 해결해야함
# 0이고 주변이 1로 둘러쌓여있으면 같은 방법으로 계산? -> dfs 해야함..

from collections import deque

W, H = map(int, input().split())
building = [list(map(int, input().split())) for _ in range(H)]
inner = 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
Q = deque()
for i in range(H):
    for j in range(W):
        if building[i][j] == 1:
            Q.append((i, j))
        else:
            cnt = 0
            for k in range(4):
                ni = i + dr[k]
                nj = j + dc[k]
                if 0 > ni or H <= ni or 0 > nj or W <= nj or building[ni][nj] == 0:
                    break
                elif 0 <= ni < H and 0 <= nj < W and building[ni][nj] == 1:
                    cnt += 1
            if cnt == 4:
                inner += 6

dre = [0, 1, 0, -1, 1, -1]
dce = [1, 0, -1, 0, 1, 1]
dro = [0, 1, 0, -1, -1, 1]
dco = [1, 0, -1, 0, -1, -1]

ans = 0
while Q:
    r, c = Q.popleft()
    if r % 2:   # 홀수 행
        for k in range(6):
            nr = r + dro[k]
            nc = c + dco[k]
            if 0 <= nr < H and 0 <= nc < W:
                if building[nr][nc] == 0:
                    ans += 1
            else:
                ans += 1
    else:       # 짝수 행
        for k in range(6):
            nr = r + dre[k]
            nc = c + dce[k]
            if 0 <= nr < H and 0 <= nc < W:
                if building[nr][nc] == 0:
                    ans += 1
            else:
                ans += 1


print(ans)
print(inner)
ans -= inner
print(ans)