# https://www.acmicpc.net/problem/2210
# DFS

def dfs(r, c, num, cnt):
    global ans
    if cnt == 6:
        ans.add(num)
        return
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if nr >= 5 or nr < 0 or nc >= 5 or nc < 0: continue
        dfs(nr, nc, num + arr[nr][nc], cnt + 1)


arr = [list(input().split()) for _ in range(5)]
ans = set()
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for i in range(5):
    for j in range(5):
        dfs(i, j, arr[i][j], 1)

print(len(ans))